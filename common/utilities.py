import requests, sys


def get_url(url):
    """
    When called pulls the api from the requested URL and send a Json Output.
    """
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    return response.json()

