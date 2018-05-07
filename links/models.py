from django.db import models


class Category(models.Model):
    """
    Table: Category
    Comment: The place to store all the categories of the link
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    Table: link
    Comment: The place to store all the links
    """
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=500)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    info = models.CharField(max_length=500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
