import requests, sys


def get_url(url, username=None, password=None):
    """
    When called pulls the api from the requested URL and send a Json Output.
    """
    # If the request needs a username & password then user the authentication
    # else just browse the URL
    if username and password:
        response = requests.get(url, auth=(username, password))
    else:
        response = requests.get(url)

    if response.status_code != 200:
        sys.exit(1)
    return response.json()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return " "
