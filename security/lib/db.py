import logging
from security.models import rssfeed


logger = logging.getLogger('roster')


def add_new_rss_feed_source(feedname, feedurl):
    """
    Method when called save the information on the rssfeed table
    """
    newfeed = rssfeed(
        feedname=feedname,
        feedurl=feedurl
    )
    newfeed.save()
    return newfeed.id


def obtain_rss_feed_items():
    """
    Method when called sends all the data from the rssFeed table.
    """
    return rssfeed.objects.all()


def obtain_rss_feed_by_id(id):
    """
    Method when called only pull the feedname & feedurl
    """
    return rssfeed.objects.filter(pk=id)
