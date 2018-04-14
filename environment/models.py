from django.db import models
from zendesk.models import Organisation


# Create your models here.
class AccountInformation(models.Model):
    """
    Table: Timeline Category
    Comment: The place to store all the Timeline Category
    """
    org_id = models.ForeignKey(Organisation, related_name='environment_account_org', on_delete=models.CASCADE, db_index=True)
    info = models.TextField()

    def __str__(self):
        return str(self.org_id)
