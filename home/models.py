from django.db import models
from zendesk.models import Organisation


class BcsTeam(models.Model):
    """
    Table: BcsTeam
    Comment: Table that stores all the BCS Team information.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    region = models.CharField(max_length=30)
    role = models.CharField(max_length=100)
    slack_handler = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    accounts = models.ManyToManyField(Organisation, related_name='bcsteam_org', blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('first_name',)


class MainPage(models.Model):
    """
    Table: MainPage
    Comment: Table that stores all the MainPage information.
    """
    page = models.CharField(max_length=30, db_index=True)
    content = models.TextField()

    def __str__(self):
        return self.page


class Certification(models.Model):
    """
    Table: Achievement
    Comment: Table that stores all the Certification information.
    """
    team_id = models.ForeignKey(BcsTeam, related_name='bcs_team_achievement',
                                on_delete=models.CASCADE, db_index=True)
    certification = models.CharField(max_length=300, null=False)

    def __str__(self):
        return str(self.team_id)