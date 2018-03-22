from django.db import models


class Organisation(models.Model):
    """
    Table: Organisation
    Comment: The place to store all the rss feeder URL
    """
    org_id = models.BigIntegerField(null=False, unique=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateField()
    location = models.CharField(max_length=20)
    expired_contract = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
