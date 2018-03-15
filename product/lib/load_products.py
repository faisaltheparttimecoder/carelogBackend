import os
from core.lib.helper import get_url
from product.lib.db import update_or_insert_products


class LoadProducts:
    def __init__(self):
        self.url = os.environ['PIVNET_BASE_URL'] + '/api/v2/products'

    def get_all_products(self):
        """
        Pull the data from the API.
        """
        data = get_url(self.url)
        return data

    def load_data_to_db(self):
        """
        From the received data load the data to the database.
        """
        data = self.get_all_products()
        for product in data['products']:
            update_or_insert_products(product)
