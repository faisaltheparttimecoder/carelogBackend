from django.db import models
from zendesk.models import Organisation


class Timeline(models.Model):
    """
    Table: Timeline
    Comment: The place to store all the Timeline
    """
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300, null=False)
    org_id = models.ForeignKey(Organisation, related_name='timeline_org', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class TimelineCategory(models.Model):
    """
    Table: Timeline Category
    Comment: The place to store all the Timeline Category
    """
    name = models.CharField(max_length=30, null=False, unique=True)
    color = models.CharField(max_length=30, null=False)
    icon = models.CharField(max_length=200, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class TimelineDetail(models.Model):
    """
    Table: Timeline Details
    Comment: The place to store all the Timeline Details
    """
    timeline_id = models.ForeignKey(Timeline, related_name='timeline', on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organisation, related_name='timeline_detail_org', on_delete=models.CASCADE)
    category_id = models.ForeignKey(TimelineCategory, related_name='category', on_delete=models.CASCADE)
    created = models.DateTimeField(null=False)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=10000, null=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

