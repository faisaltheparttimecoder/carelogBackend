from django.db import models


class LastRun(models.Model):
    """
    Table: Lastrun
    Comment: Table that stores all the background runner last run.
    """
    component = models.CharField(max_length=30)
    last_run = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.component


class BackupHistory(models.Model):
    """
    Table: backup_history
    Comment: Table that stores all the backup information ...
    """

    backup_date = models.DateTimeField(null=False)
    backup_status = models.CharField(max_length=20, null=False)
    backup_file = models.CharField(max_length=200, null=False)
    backup_size = models.IntegerField(default=0)

    def __str__(self):
        return str(self.backup_date) + "(" + str(self.backup_status) + ")"

    def backup_size_in_kb(self):
        return int(self.backup_size) / 1024
