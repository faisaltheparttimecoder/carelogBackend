import feedparser, logging, json
from django.core import serializers
from security.lib.db import obtain_rss_feed_items, obtain_rss_feed_by_id

logger = logging.getLogger('carelog')


class Feeder:

    def __init__(self):
        """
        Initialize all the variable here.
        """
        self.collector = {
            'items': [],
            'contents': {},
            'selected_item': '',
            'selected_route': ''
        }

    def obtain_stored_rss_items(self):
        """
        Read the data from the database and update the collector on the information.
        """
        logger.info("Requesting all the data from the rssfeed table")
        rssItems = obtain_rss_feed_items()
        self.collector['items'] = json.loads(serializers.serialize('json', rssItems))

    def is_rssitem_none(self, fiterItem):
        """
        If the filter item is none, then pass the default item
        """
        logger.info("Pulling the rss item based on user request")
        if len(self.collector['items']) > 0:  # Page Refresh, so send default
            if fiterItem == '0':
                logger.info("Page refresh, so picking the default value")
                self.collector['selected_item'] = self.collector['items'][0]['fields']['name']
                self.collector['selected_route'] = self.collector['items'][0]['fields']['url']
            else:
                logger.info("User request information from a particular feed")
                rssfeed = obtain_rss_feed_by_id(fiterItem)
                feed = json.loads(serializers.serialize('json', rssfeed))[0]
                if len(feed) > 0:
                    self.collector['selected_item'] = feed['fields']['name']
                    self.collector['selected_route'] = feed['fields']['url']
                else:
                    return None
        else:
            return None

    def get_rss_content(self):
        """
        Using FeedParser get the entries of the RSS Feed.
        """
        logger.info("Extract RSS content based on the selected rss feed: {0}".format(self.collector['selected_route']))
        rss_content = feedparser.parse(self.collector['selected_route'])
        self.collector['contents'] = rss_content['entries']

    def rss_feeder(self, fiterItem):
        """
        Rss feeder work flow.
        """

        # First obtain the stored rss information.
        self.obtain_stored_rss_items()

        # Is there any specific rss content request.
        self.is_rssitem_none(fiterItem)

        # Get rss content
        self.get_rss_content()

        # Return the data as Json
        return self.collector

