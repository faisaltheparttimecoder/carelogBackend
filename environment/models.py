from django.db import models
from zendesk.models import Organisation
from products.models import Product
from timeline.models import Timeline


# Create your models here.
class AccountInformation(models.Model):
    """
    Table: Account Information
    Comment: The place to store all the Account Information
    """
    org_id = models.ForeignKey(Organisation, related_name='environment_account_org', on_delete=models.CASCADE, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return str(self.org_id)


class ContactInformation(models.Model):
    """
    Table: Contact Information
    Comment: The place to store all the Contact Information
    """
    org_id = models.ForeignKey(Organisation, related_name='environment_contact_org', on_delete=models.CASCADE, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return str(self.org_id)


class EnvironmentNote(models.Model):
    """
    Table: Environment Notes
    Comment: The place to store all the Environment Notes
    """
    org_id = models.ForeignKey(Organisation, related_name='environment_notes_org', on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(default="Add notes to this note section", blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return str(self.org_id)


class EnvironmentProductsList(models.Model):
    """
    Table: Environment Products List
    Comment: The place to store all the Environment Products List
    """
    org_id = models.ForeignKey(Organisation, related_name='environment_product_list_org', on_delete=models.CASCADE, db_index=True)
    products = models.ManyToManyField(Product, related_name='environment_product_list', blank=True)

    def __str__(self):
        return str(self.org_id)


class EnvironmentType(models.Model):
    """
    Table: Environment Type
    Comment: The place to store all the Environment Type
    """
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.type)


class EnvironmentInstance(models.Model):
    """
    Table: Environment Instance
    Comment: The place to store all the Environment Instance
    """
    type_id = models.ForeignKey(EnvironmentType, related_name='environment_type', on_delete=models.CASCADE, db_index=True)
    org_id = models.ForeignKey(Organisation, related_name='environment_instance_org', on_delete=models.CASCADE,
                               db_index=True)
    timeline_id = models.ForeignKey(Timeline, related_name='environment_timeline', on_delete=models.SET_NULL,
                                    db_index=True, null=True)
    name = models.CharField(max_length=50)
    infrastructure = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('org_id', 'name', 'infrastructure'),)

    def __str__(self):
        return str(self.name)


class EnvironmentInstanceProduct(models.Model):
    """
    Table: Environment Instance
    Comment: The place to store all the Environment Instance Product
    """
    instance_id = models.ForeignKey(EnvironmentInstance, related_name='environment_instance', on_delete=models.CASCADE,
                                    db_index=True)
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name)