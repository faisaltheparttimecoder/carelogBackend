import logging
from security.models import rssfeed


logger = logging.getLogger('roster')


def add_new_rss_feed_source(feedname, feedurl):
    """
    Method when called save the information on the rssfeed table
    """
    logger.info("Recording new rss feed source")
    newfeed = rssfeed(
        name=feedname,
        url=feedurl
    )
    newfeed.save()
    return newfeed.id


def obtain_rss_feed_items():
    """
    Method when called sends all the data from the rssFeed table.
    """
    logger.info("Sending all the data from the rssfeed table")
    return rssfeed.objects.all()


def obtain_rss_feed_by_id(id):
    """
    Method when called only pull the feedname & feedurl
    """
    logger.info("Filtering the data from the rssfeed table based on the PK: {0}".format(id))
    return rssfeed.objects.filter(pk=id)
