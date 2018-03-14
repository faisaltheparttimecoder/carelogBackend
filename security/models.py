from django.db import models


class rssfeed(models.Model):
    """
    Table: rssfeed
    Comment: The place to store all the rss feeder URL
    """
    feedname = models.CharField(max_length=2000, null=False, unique=True)
    feedurl = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.feedname
