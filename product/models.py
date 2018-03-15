from django.db import models


class product(models.Model):
    """
    Table: product
    Comment: The place to store all the Pivotal Network Products
    """
    name = models.CharField(max_length=2000, null=False, unique=True)
    slug = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=400, null=False)

    def __unicode__(self):
        return self.name
