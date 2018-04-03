#!/usr/bin/env bash

# Script parameters
export sleeper=60

# Getting up the directory path
echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Getting the directory path"
export script=$0
export script_basename=`basename $script`
export script_dir=`dirname $script`
cd ${script_dir}
export script_dir=`pwd`
export carelog_base=${script_dir}/../..
cd ${carelog_base}
export carelog_base=`pwd`

# Executing the django script in a loop.
while true
do
    echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Executing the background task..."
        python ${carelog_base}/manage.py shell < $script_dir/django_shell.py
    echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Sleeping ..."
        sleep ${sleeper}
    echo "`date +"%Y-%m-%d %H:%M:%S"`: INFO - Waking up..."
done
