import os, logging, copy
from datetime import datetime, timedelta
from time import gmtime, strftime
from zendesk.models import Organisation, Ticket, LastOrgTicketLoaderRun
from common.utilities import get_url

logger = logging.getLogger('carelog')


class LoadTickets:
    def __init__(self):
        """
        Initialize all the environment variable
        """
        self.url = os.environ['ZENDESK_BASE_URL'] + '/api/v2/search'
        self.search_query = self.url + '?page={0}&query=type:ticket organization:{1} updated>={2} updated<={3}'
        self.now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.until = self.now[0:10] + 'T' + self.now[11:19] + 'Z'
        self.store_username_temp = {}

    def extract_saved_org(self):
        """
        Extract all the org, that we care about
        """
        logger.info("Pull all the saved DSE Org ID")
        return Organisation.objects.all()

    def extract_last_loader_run(self, org_id):
        """
        Obtain the information until when the loader was run.
        """
        logger.info("Pull all last recoded time of the org: {0}".format(org_id))
        return LastOrgTicketLoaderRun.objects.filter(org_id=Organisation.objects.get(org_id=org_id)).filter(success=True).order_by('-runtime')[:1]

    def ticket_skeletion(self):
        """
        Below is the information that we need
        """
        return {
            'ticket_id': '',
            'org_id': '',
            'created_at': '',
            'updated_at': '',
            'priority': 'Unknown',
            'status': 'Unknown',
            'submitter': 'Unknown',
            'assignee': 'Unknown',
            'product': 'Unknown',
            'kb': 'Unknown',
            'resolution_code': 'Unknown',
            'defect': 'Unknown',
            'product_version': 'Unknown',
            'product_component': 'Unknown',
            'product_component_category': 'Unknown',
            'iaas': 'Unknown',
            'environment': 'Unknown',
            'type': 'Unknown'
        }

    def transform_data(self, result, storage):
        """
        Transform the API response to database table
        """

        for custom_field in result['custom_fields']:

            # For every product
            if custom_field['id'] == 22788182 and custom_field['value']:
                storage['product'] = custom_field['value']
            # For CSR Team
            elif custom_field['id'] == 23954923 and custom_field['value'] and storage['product'] == 'Unknown':
                storage['product'] = custom_field['value']

            # Get the priority of the ticket
            if custom_field['id'] == 23872527:
                storage['priority'] = custom_field['value']

            # Is KB field is filled for this ticket
            if custom_field['id'] == 30226808 and custom_field['value']:
                storage['kb'] = custom_field['value']

            # If Resolution code
            if custom_field['id'] == 31485838 and custom_field['value']:
                storage['resolution_code'] = custom_field['value']

            # If environment
            if custom_field['id'] == 27146757 and custom_field['value']:
                storage['environment'] = custom_field['value']

            # If JIRA Open
            if custom_field['id'] == 27129838 and custom_field['value']:
                storage['related_ticket'] = custom_field['value']

            # IaaS Information
            if custom_field['id'] == 37501628 and custom_field['value']:
                storage['iaas'] = custom_field['value']

            # Ticket Type Information
            if custom_field['id'] == 23957413 and custom_field['value']:
                storage['type'] = custom_field['value']

            # Get the product version
            # Hadoop
            if custom_field['id'] == 27971777 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            elif custom_field['id'] == 25263147 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # Gemfire / GPDB
            elif custom_field['id'] == 23785228 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # GPDB
            elif custom_field['id'] == 24104873 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # Gemfire
            elif custom_field['id'] == 29072088 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # Gemfire XD
            elif custom_field['id'] == 29072918 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # tcserver
            elif custom_field['id'] == 29140638 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # webserver
            elif custom_field['id'] == 29160217 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # spring
            elif custom_field['id'] == 29140358 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # pcf
            elif custom_field['id'] == 29084107 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # rabbitmq
            elif custom_field['id'] == 29140548 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # GPCC
            elif custom_field['id'] == 29084687 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # VRP
            elif custom_field['id'] == 29084577 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # Tracker CF
            elif custom_field['id'] == 29072908 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # Pivotal R
            elif custom_field['id'] == 29083377 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # GpText
            elif custom_field['id'] == 29084607 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]
            # Chorus
            elif custom_field['id'] == 29083367 and custom_field['value']:
                storage['product_version'] = str(custom_field['value'])[0:100]

            # Sub Component of the product
            # Hadoop
            if custom_field['id'] == 26295827 and custom_field['value']:
                storage['product_component'] = custom_field['value']
            elif custom_field['id'] == 26272388 and custom_field['value']:
                storage['product_component'] = custom_field['value']
            # Gemfire
            elif custom_field['id'] == 31509268 and custom_field['value']:
                storage['product_component'] = custom_field['value']
            # GPDB
            elif custom_field['id'] == 26141598 and custom_field['value']:
                storage['product_component'] = custom_field['value']
            # pcf
            elif custom_field['id'] == 31511837 and custom_field['value']:
                storage['product_component'] = custom_field['value']
            # Gemfire XD
            elif custom_field['id'] == 31509988 and custom_field['value']:
                storage['product_component'] = custom_field['value']
            # CSR
            elif custom_field['id'] == 23942478 and custom_field['value'] and storage['product_component'] == 'Unknown':
                storage['product_component'] = custom_field['value']

            # product component category
            # ERT
            if custom_field['id'] == 31488098 and custom_field['value']:
                storage['product_component_category'] = custom_field['value']
            # OpsManager
            elif custom_field['id'] == 31511937 and custom_field['value']:
                storage['product_component_category'] = custom_field['value']
            # Buildpack
            elif custom_field['id'] == 31507778 and custom_field['value']:
                storage['product_component_category'] = custom_field['value']

        return storage

    def get_username(self, user_id):
        """
        Get the username based on the user id
        """
        logger.debug("Extracting the username for the user ID: {0}".format(user_id))
        user_id = str(user_id)
        if user_id in self.store_username_temp:
            return self.store_username_temp[user_id]
        else:
            url = os.environ['ZENDESK_BASE_URL'] + '/api/v2/users/{0}.json'
            url = url.format(user_id)
            user = get_url(url, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD'])
            self.store_username_temp[user_id] = user['user']['name']
            return user['user']['name']

    def populate_to_db_table(self, data):
        """
        Commit the record to the database
        """
        try:
            exists = Ticket.objects.get(ticket_id=data['ticket_id'])
            Ticket.objects.filter(ticket_id=data['ticket_id']).update(
                ticket_id=data['ticket_id'],
                org_id=Organisation.objects.get(org_id=data['org_id']),
                created=data['created_at'],
                updated=data['updated_at'],
                priority=data['priority'],
                status=data['status'],
                submitter=data['submitter'],
                assignee=data['assignee'],
                product=data['product'],
                kb=data['kb'],
                resolution_code=data['resolution_code'],
                defect=data['defect'],
                product_version=data['product_version'],
                product_component=data['product_component'],
                product_component_category=data['product_component_category'],
                iaas=data['iaas'],
                environment=data['environment'],
                type=data['type']
            )
        except Ticket.DoesNotExist:
            Ticket.objects.create(
                ticket_id=data['ticket_id'],
                org_id=Organisation.objects.get(org_id=data['org_id']),
                created=data['created_at'],
                updated=data['updated_at'],
                priority=data['priority'],
                status=data['status'],
                submitter=data['submitter'],
                assignee=data['assignee'],
                product=data['product'],
                kb=data['kb'],
                resolution_code=data['resolution_code'],
                defect=data['defect'],
                product_version=data['product_version'],
                product_component=data['product_component'],
                product_component_category=data['product_component_category'],
                iaas=data['iaas'],
                environment=data['environment'],
                type=data['type']
            )

    def record_last_run(self, org, since, outcome, until):
        """
        Whatever the outcome record the time
        """
        LastOrgTicketLoaderRun.objects.create(
            org_id=Organisation.objects.get(org_id=org),
            last=datetime.strptime(since, "%Y-%m-%dT%H:%M:%SZ"),
            success=outcome,
            runtime=until
        )

    def build_data(self, org, results_data):
        """
        Prepare data from the API generated.
        """
        for result in results_data['results']:
            temp = copy.deepcopy(self.ticket_skeletion())
            logger.debug("Extracting information of the ticket: {0}".format(result['id']))
            temp['ticket_id'] = result['id']
            temp['org_id'] = org
            temp['created_at'] = datetime.strptime(result['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            temp['updated_at'] = datetime.strptime(result['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            temp['status'] = result['status']
            temp['submitter'] = self.get_username(result['submitter_id'])
            temp['assignee'] = self.get_username(result['assignee_id'])
            table_content = self.transform_data(result, temp)
            self.populate_to_db_table(table_content)

    def get_api(self, page, org, last, until):
        """
        Now using the org and last run get the information of ticket
        """
        try:
            url = self.search_query.format(page, org, last, until)
            logger.info("Extracting data from the url: {0}".format(url))
            data = get_url(url, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD'])
            self.build_data(org, data)
            if data['next_page'] and data['next_page'] != url:
                return self.get_api(page + 1, org, last, until)
        except Exception as e:
            logger.info("Failed to load the ticket information, the error is: {0}".format(e))
            return False
        return True

    def remove_recently_added_flag(self, org):
        """
        Update the org table that the dashboard is ready.
        """
        Organisation.objects.filter(org_id=org).update(recently_added=False)

    def extract_data(self):
        """
        For all the org check when was the last time we ran the loader
        and then start the process to extract the data
        """
        logger.info("Extracting tickets for all the saved orgs")
        for org in self.extract_saved_org():

            page = 1
            org_id = org.org_id
            last_run_data = self.extract_last_loader_run(org_id)
            logger.debug("Pulling all the tickets for the org (org ID): {0} ({1})".format(org, org_id))
            if last_run_data.count() == 0:  # No data, new org added
                last_run_date = '2001-01-01T00:00:00Z'
            else:   # We have time when we last run the loader
                last_run_date = ""
                for last_run in last_run_data:
                    last_run_date = str(last_run.runtime - timedelta(minutes=30))
                    last_run_date = last_run_date[0:10] + 'T' + last_run_date[11:19] + 'Z'

            logger.debug("Last ticket collection run for this org: {0}".format(
                datetime.strptime(last_run_date, "%Y-%m-%dT%H:%M:%SZ"))
            )
            if self.get_api(page, org_id, last_run_date, self.until):
                outcome = True
                self.remove_recently_added_flag(org_id)
                logger.info("The run to get the information of the org({0}) is {1}".format(org_id, outcome))
            else:
                outcome = False
                logger.error("The run to get the information of the org({0}) is {1}".format(org_id, outcome))

            logger.info("Recording the runtime & outcome of this run for the org: {0}".format(org_id))
            self.record_last_run(org_id, last_run_date, outcome, self.now)
