from django.db import models


class Resource(models.Model):
    """
    Table: Resource
    Comment: The place to store all the Resource information
    """
    name = models.CharField(max_length=100, unique=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, null=False)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

