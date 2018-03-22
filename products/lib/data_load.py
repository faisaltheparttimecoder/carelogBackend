import os
from django.db.models import Q
from products.models import Product
from common.utilities import get_url


class LoadProducts:

    def __init__(self):
        """
        Initialize the variable here.
        """
        self.url = os.environ['PIVNET_BASE_URL'] + '/api/v2/products'

    def update_or_insert_products(self, data):
        """
        Check if the data exists, if yes then update it else insert into it
        """
        piv_product = data['name']
        piv_slug = data['slug']
        exists = Product.objects.filter(name=data)
        if exists:
            Product.objects.filter(Q(name=piv_product) | Q(slug=piv_slug)).update(
                name=piv_product,
                slug=piv_slug,
                url=data['_links']['releases']['href']
            )
        else:
            new_product = Product(
                name=piv_product,
                slug=data['slug'],
                url=data['_links']['releases']['href']
            )
            new_product.save()

    def load_data_to_db(self):
        """
        From the received data load the data to the database.
        """
        data = get_url(self.url)
        for product in data['products']:
            self.update_or_insert_products(product)
