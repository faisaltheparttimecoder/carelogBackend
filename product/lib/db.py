import logging
from django.db.models import Q
from product.models import product

logger = logging.getLogger('carelog')


def send_all_products():
    """
    Send all the data it has on the products table.
    """
    logger.info("Requesting all the data from the table product")
    return product.objects.all().order_by('name')


def filter_product_by_name(data):
    """
    Return the data based on the product filter(by name)
    """
    logger.info("Filtering the data from the table product using the name filter: {0}".format(data))
    return product.objects.filter(name=data)


def filter_product_by_id(id):
    """
    Return the data based on the product filter (by ID)
    """
    logger.info("Filtering the data from the table product using the ID filter: {0}".format(id))
    return product.objects.filter(pk=id)


def update_or_insert_products(data):
    """
    Check if the data exists, if yes then update it else insert into it
    """
    logger.info("Loading / Refreshing the product table")
    piv_product = data['name']
    piv_slug = data['slug']
    exists = filter_product_by_name(piv_product)
    if exists:
        logger.info("Data exists, updating the record")
        product.objects.filter(Q(name=piv_product) | Q(slug=piv_slug)).update(
            name=piv_product,
            slug=piv_slug,
            url=data['_links']['releases']['href']
        )
    else:
        logger.info("Data doesn't exists, inserting the record")
        new_product = product(
            name=piv_product,
            slug=data['slug'],
            url=data['_links']['releases']['href']
        )
        new_product.save()


