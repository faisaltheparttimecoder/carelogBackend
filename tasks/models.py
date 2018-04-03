from django.db import models

class LastRun(models.Model):
    """
    Table: Lastrun
    Comment: Table that stores all the background runner last run.
    """
    component = models.CharField(max_length=30)
    last_run = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.component
