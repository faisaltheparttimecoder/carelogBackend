from django.db import connection, transaction
from zendesk.models import LastOrgTicketLoaderRun
import datetime

cursor = connection.cursor()


class Maintenance:
    def __init__(self):
        self.table_list = [
            'auth_group',
            'auth_group_permissions',
            'auth_permission',
            'auth_user',
            'auth_user_groups',
            'auth_user_user_permissions',
            'django_admin_log',
            'django_content_type',
            'django_migrations',
            'django_session',
            'environment_accountinformation',
            'environment_contactinformation',
            'environment_environmentinstance',
            'environment_environmentinstanceproduct',
            'environment_environmentnote',
            'environment_environmentproductslist',
            'environment_environmentproductslist_products',
            'environment_environmenttype',
            'home_bcsteam',
            'home_bcsteam_accounts',
            'home_certification',
            'home_feedback',
            'home_mainpage',
            'links_category',
            'links_link',
            'oauth2_provider_accesstoken',
            'oauth2_provider_application',
            'oauth2_provider_grant',
            'oauth2_provider_refreshtoken',
            'products_product',
            'resources_resource',
            'security_rssfeed',
            'social_auth_association',
            'social_auth_code',
            'social_auth_nonce',
            'social_auth_partial',
            'social_auth_usersocialauth',
            'tasks_backuphistory',
            'tasks_lastrun',
            'timeline_timeline',
            'timeline_timelinecategory',
            'timeline_timelinedetail',
            'zendesk_lastorgticketloaderrun',
            'zendesk_organisation',
            'zendesk_ticket',
            'zendesk_ticketattribute',
            'zendesk_ticketnote'
        ]

        # Keep the space, do not remove
        self.maintenance_tasks = [
            'OPTIMIZE TABLE ', 'ANALYZE TABLE ', 'CHECK TABLE ', 'CHECKSUM TABLE '
        ]

        # Delete data from the historical table, if its n days old (one week old)
        self.n_days = 7

    def date_diff(self):
        """
        Provide difference of date based on the number of days required to purge
        """
        return datetime.datetime.now() - datetime.timedelta(days=self.n_days)

    def cleanup_older_data(self):
        """
        Cleaning up old stale historical data
        """
        purge_dates = self.date_diff()
        LastOrgTicketLoaderRun.objects.filter(last__lte=purge_dates).delete()

    def execute_command(self, table):
        """
        Execute table maintenance tasks
        """
        for task in self.maintenance_tasks:
            command = task + table
            cursor.execute(command)
            transaction.commit()

    def run_table_maintenance(self):
        """
        Start the table maintenance program ...
        """
        # Cleanup older data
        self.cleanup_older_data()

        # Maintenance task
        for table in self.table_list:
            self.execute_command(table)

        # Close cursor once done
        connection.close()