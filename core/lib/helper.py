import requests, logging, sys

logger = logging.getLogger('carelog')


def get_url(url):
    """
    When called pulls the api from the requested URL
    """
    logger.info("Requesting data from API URL: {0}".format(url))
    response = requests.get(url)
    if response.status_code != 200:
        logger.error("API ERROR: URL({0}), RETURN:{1}, EXPECTED:{2}".format(url, 200, response.status_code))
        sys.exit(1)
    return response.json()
