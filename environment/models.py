from django.db import models
from zendesk.models import Organisation


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
    info = models.TextField(default="Add notes to this note section", blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return str(self.org_id)