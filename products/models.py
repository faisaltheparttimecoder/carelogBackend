from django.db import models


class Product(models.Model):
    """
    Table: product
    Comment: The place to store all the Pivotal Network Products
    """
    name = models.CharField(max_length=2000, null=False, unique=True)
    slug = models.CharField(max_length=200, null=False)
    url = models.URLField(max_length=500, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
