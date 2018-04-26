#!/usr/bin/env bash

# Getting up the directory path
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Getting the directory path"
export script=$0
export script_basename=`basename $script`
export carelog_bin_dir=`dirname $script`
cd ${carelog_bin_dir}
export carelog_bin_dir=`pwd`
export carelog_base=${carelog_bin_dir}/..
cd ${carelog_base}
export carelog_base=`pwd`

# Backup / log Directory
export carelog_backup_dir=${carelog_base}/backup
export carelog_log_dir=${carelog_base}/log

# Create log or backup directory if doesnt exists
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Create backup / log directory if it doesnt not exists"
if [ ! -d ${carelog_backup_dir} ]; then
    mkdir -p ${carelog_backup_dir}
fi
if [ ! -d ${carelog_log_dir} ]; then
    mkdir -p ${carelog_log_dir}
fi

# Dump file / logfile name
export dump_file=${carelog_backup_dir}/carelog-backup-`date +"%m-%d-%y-%H-%M-%S"`.dmp
export logfile=${carelog_log_dir}/carelog-backup-`date +"%m-%d-%y-%H-%M-%S"`.dmp

# Set the environment variable
source ${carelog_bin_dir}/environment.env

# CF Command line arguments to login to cf
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Checking if the cf executable is installed"
if ! [ -x "$(command -v cf)" ]; then
  echo 'ERROR: cf executable is not installed.' >&2
  exit 1
fi

# Terminate old process that is running on the port ( for eg.s if the backup failed last time )
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Terminating old process if running on the port"
netstat -nlp | grep ${local_port} | awk '{print $7}' | cut -d'/' -f1 | xargs -n1 /bin/kill 2> /dev/null

# CF Command line arguments to login to cf
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Login to PWS"
`command -v cf` login -u ${username} -p `echo ${user_token} | openssl enc -aes-256-cbc -a -d -salt -pass pass:tecmint` -a ${api_url} -o ${org} -s ${space}

# Skipping the below steps since we have now migrated from MySQL v1 to MySQL v2 which is has more disk space and
# throughput (i.e v2 is dedicated instance )

## Install cf mysql plugin
#echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Install Mysql / mysqldump plugin"
#`command -v cf` install-plugin -r "CF-Community" mysql-plugin -f

## Check if MySQL CF Plugin is installed is installed
#echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Checking if the cf MySQLDump plugin is installed"
#mysql_plugin_installed=`\`command -v cf\` plugins | grep mysqldump | wc -l | tr -d ' '`
#if [ ${mysql_plugin_installed} -gt 0 ]; then
#    echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - cf MySQLDump plugin is installed, continue..."
#else
#    echo "`date +"%Y-%m-%d %H:%M:%S"`: ERROR - cf MySQLDump plugin is not installed, exiting..."
#    exit 1
#fi

# Open a ssh tunnel for reading the data from the database.
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Creating a SSH tunnel"
`command -v cf` ssh -N -L ${local_port}:${source_host}:${source_port} ${app_name} &

# Store the background process PID
export tunnel_pid=$!

# Sleep for 10 seconds for tunnel to establish
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Sleeping for 10 seconds for ssh tunnel to establish"
sleep 10

# Everything is good, now time to execute the backup
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Running cf MySQLDump to take the backup of the database: ${db}"
#`command -v cf` mysqldump ${service_name} > ${dump_file}
mysqldump  -h ${local_host} --port=${local_port} --user="${dbusername}" --password="${dbpassword}" ${db} > ${dump_file}
retcode=$?
if [ ${retcode} -ne 0 ]; then
    export status_message="FAILURE"
    echo "`date +"%Y-%m-%d %H:%M:%S"`: ERROR - The database backup failed .."
else
    export status_message="SUCCESS"
    echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - The database backup has successfully completed.."
fi

# Gzip the mysql database dump file
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Compressing the backup"
gzip ${dump_file}
retcode=$?
if [ ${retcode} -ne 0 ]; then
    export status_message="FAILURE"
    echo "`date +"%Y-%m-%d %H:%M:%S"`: ERROR - The compression of backup failed ...."
fi

# Remove backup that is greater than retention date
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Removing older backup that is longer than the retention period:" ${retention}
find ${carelog_backup_dir} -type f -mtime +${retention} -exec rm -rf {} +

# size of the dump
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Getting the size of the dump ..."
if [  -f ${dump_file}.gz ]; then
    export dump_size=`stat -c %s ${dump_file}.gz`
else
    export status_message="FAILURE"
    echo "`date +"%Y-%m-%d %H:%M:%S"`: ERROR - Cannot file the stat of the file .."
fi

# Updating the database with the status of the backup
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Attempting to store the information about this backup in the carelog database ..."
if [ ${status_message} ==  "FAILURE" ]; then
    export sql_query="insert into tasks_backuphistory (backup_date, backup_status, backup_file, backup_size)  values (now(), '${status_message}', '${dump_file}.gz', 0)"
else
    export sql_query="insert into tasks_backuphistory (backup_date, backup_status, backup_file, backup_size)  values (now(), '${status_message}', '${dump_file}.gz', '${dump_size}')"
fi
#echo ${sql_query} | `command -v cf` mysql ${service_name}
echo ${sql_query} | mysql -h ${local_host} --port=${local_port} --user="${dbusername}" --password="${dbpassword}" ${db}

# Terminate the background process
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Terminating the backup process"
kill ${tunnel_pid} 2> /dev/null

# Logout from CF and cleanup the files
`command -v cf` logout
rm -rf ${HOME}/.cf

# Success message
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Carelog database backup is completed"
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - The location and filename of the backup is \""${dump_file}"\""