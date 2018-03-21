from django.db import models


class RssFeed(models.Model):
    """
    Table: rssfeed
    Comment: The place to store all the rss feeder URL
    """
    name = models.CharField(max_length=100, null=False, unique=True)
    url = models.URLField(max_length=500, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
