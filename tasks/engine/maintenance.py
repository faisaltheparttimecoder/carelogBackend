from django.db import connection, transaction
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
            'links_category',
            'links_link',
            'oauth2_provider_accesstoken',
            'oauth2_provider_application',
            'oauth2_provider_grant',
            'oauth2_provider_refreshtoken',
            'products_product',
            'security_rssfeed',
            'social_auth_association',
            'social_auth_code',
            'social_auth_nonce',
            'social_auth_partial',
            'social_auth_usersocialauth',
            'tasks_lastrun',
            'timeline_timeline',
            'timeline_timelinecategory',
            'timeline_timelinedetail',
            'zendesk_hotticket',
            'zendesk_organisation',
            'zendesk_ticketnote',
        ]

        # Keep the space, do not remove
        self.maintenance_tasks = [
            'OPTIMIZE TABLE ', 'ANALYZE TABLE ', 'CHECK TABLE ', 'CHECKSUM TABLE '
        ]

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

        # Maintenance task
        for table in self.table_list:
            self.execute_command(table)

        # Close cursor once done
        connection.close()