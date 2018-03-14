import logging
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from security.lib.db import add_new_rss_feed_source
from security.lib.feeder import Feeder

logger = logging.getLogger('carelog')


def security(request, rssItem):
    """
    Main function that sends all the RSS feeds...
    """
    logging.info("Request received to provide the RSS Feed")
    return JsonResponse(Feeder().rss_feeder(rssItem))


@csrf_exempt
def new_rss_feed(request):
    """
    When called it adds in the new RSS Feed source
    """
    logging.info("Request received to add source of a new RSS Feed")
    if request.method == "POST":
        try:
            logging.info("Post Request: Committing the data to the database")
            new_rss_feed_data = dict(request.POST)
            feedname = new_rss_feed_data['feedname'][0]
            feedurl = new_rss_feed_data['feedurl'][0]
            saved_id = add_new_rss_feed_source(feedname, feedurl)
            return JsonResponse({
                'id': saved_id,
                'message': 'success'
            })
        except Exception as e:
            return JsonResponse({
                'id': 000,
                'message': str(e)
            })
    else:
        logging.info("Get Request: Sending failure message")
        return HttpResponse('failure')


