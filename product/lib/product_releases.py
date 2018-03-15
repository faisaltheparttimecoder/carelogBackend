import logging, json
from django.core import serializers
from product.lib.db import send_all_products, filter_product_by_id
from core.lib.helper import get_url

logger = logging.getLogger('carelog')


class PivotalRelease:

    def __init__(self):
        """
        Initialize all the global class parameter here.
        """
        self.collector = {
            'items': [],
            'contents': {},
            'selected_item': '',
            'selected_route': ''

        }

    def extract_all_products(self):
        """
        Extracting all the pivotal products
        """
        logging.info("Extracting all the pivotal products")
        all_products = send_all_products()
        self.collector['items'] = json.loads(serializers.serialize('json', all_products))

    def is_product_selected(self, selected_product):
        """
        Send data based on customer selection.
        """
        logging.info("Send data based on what users have selected")
        if len(self.collector['items']) > 0:  # Page Refresh, so send default
            if selected_product == '0':
                logger.info("Page refresh, so picking the default value")
                self.collector['selected_item'] = self.collector['items'][0]['fields']['name']
                self.collector['selected_route'] = self.collector['items'][0]['fields']['url']
            else:
                logger.info("User request information from a particular product")
                product_selected = filter_product_by_id(selected_product)
                selected = json.loads(serializers.serialize('json', product_selected))[0]
                if len(selected) > 0:
                    self.collector['selected_item'] = selected['fields']['name']
                    self.collector['selected_route'] = selected['fields']['url']
                else:
                    return None
        else:
            return None

    def get_product_contents(self):
        """
        Pulling data of all releases on the product
        """
        logger.info("Extract RSS content based on the selected product: {0}".format(self.collector['selected_route']))
        rss_content = get_url(self.collector['selected_route'])
        self.collector['contents'] = rss_content['releases']

    def product_releases(self, product_id):
        """
        Rss feeder work flow.
        """

        # First obtain the stored product information.
        self.extract_all_products()

        # Is there any specific product request.
        self.is_product_selected(product_id)

        # Get rss content
        self.get_product_contents()

        # Return the data as Json
        return self.collector
