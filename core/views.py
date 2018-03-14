import logging
from django.http import JsonResponse, HttpResponse

# Initialize logger here
logger = logging.getLogger('carelog')
logging.basicConfig(format='%(asctime)s:[%(levelname)s]: %(message)s', level=logging.INFO)


def login(request):
    return HttpResponse('sucess')