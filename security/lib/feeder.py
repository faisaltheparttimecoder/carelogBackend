import feedparser, logging
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
        rssItems = obtain_rss_feed_items()
        for rssItem in rssItems:
            temp = {
                'id': rssItem.pk,
                'item': rssItem.feedname,
                'route': rssItem.feedurl
            }
            self.collector['items'].append(temp)

    def is_rssitem_none(self, fiterItem):
        """
        If the filter item is none, then pass the default item
        """
        if len(self.collector['items']) > 0:
            if fiterItem == '0':
                self.collector['selected_item'] = self.collector['items'][0]['item']
                self.collector['selected_route'] = self.collector['items'][0]['route']
            else:
                rssfeed = obtain_rss_feed_by_id(fiterItem)
                for feed in rssfeed:
                    self.collector['selected_item'] = feed.feedname
                    self.collector['selected_route'] = feed.feedurl
        else:
            return None

    def get_rss_content(self):
        """
        Using FeedParser get the entries of the RSS Feed.
        """
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

