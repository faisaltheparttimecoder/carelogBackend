import datetime, os
from django.contrib.auth.models import User
from products.lib.data_load import LoadProducts
from tasks.engine.maintenance import Maintenance
from tasks.models import LastRun


class TaskRunner:

    def __init__(self):
        """
        Initialize the variables.
        """
        self.admin_username = 'admin'
        self.admin_email = 'admin@email.com'
        self.admin_pass = os.environ['ADMIN_PASS']
        self.when_to_run = {
            'refresh_pivotal_products_table': 3600,     # Every Hour
            'table_maintenance': 86400,  # Once a day
        }

    def update_last_run_time(self, component):
        """
        Once the component run is completed update the lastrun table, if
        its running for the first time, then set the time now.
        """
        if LastRun.objects.filter(component=component).count() == 0:
            run = LastRun(component=component)
            run.save()
        else:
            LastRun.objects.filter(component=component).update(
                last_run=datetime.datetime.now()
            )

    def check_last_run_table(self, component):
        """
        Get all the date/time of the last run by components ..
        """
        last_record_time = '2000-01-01 00:00:00'
        last_record_time = datetime.datetime.strptime(last_record_time, "%Y-%m-%d %H:%M:%S")
        last_record_time = (datetime.datetime.now() - last_record_time).total_seconds()
        last_run = LastRun.objects.filter(component=component).values('last_run')
        for last_run in last_run:
            last_record_time = (datetime.datetime.now() - last_run['last_run']).total_seconds()
        return last_record_time

    def create_super_user(self):
        """
        Create SuperUser if not exits
        """

        if User.objects.filter(username=self.admin_username).count() == 0:
            User.objects.create_superuser(self.admin_username, self.admin_email, self.admin_pass)

    def run_refresh_pivotal_products_table(self):
        """
        Run the component to load all the pivotal products
        """
        if self.when_to_run['refresh_pivotal_products_table'] < self.check_last_run_table('refresh_pivotal_products_table'):
            LoadProducts().load_data_to_db()
            self.update_last_run_time('refresh_pivotal_products_table')

    def run_check_for_table_maintenance(self):
        """
        Run the component to do table maintainence ...
        """
        if self.when_to_run['table_maintenance'] < self.check_last_run_table('table_maintenance'):
            Maintenance().run_table_maintenance()
            self.update_last_run_time('table_maintenance')

    def run_task(self):
        """
        Execute all the tasks ...
        """
        self.create_super_user()
        self.run_refresh_pivotal_products_table()
        self.run_check_for_table_maintenance()
