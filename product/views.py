import logging
from django.http import JsonResponse
from product.lib.product_releases import PivotalRelease

logger = logging.getLogger('carelog')


def products(request, product_id):
    logger.info("Requesting to provide all the product list...")
    return JsonResponse(PivotalRelease().product_releases(product_id))