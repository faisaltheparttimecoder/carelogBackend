from django.db import models


class Organisation(models.Model):
    """
    Table: Organisation
    Comment: The place to store all the Organization
    """
    org_id = models.BigIntegerField(null=False, unique=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateField()
    location = models.CharField(max_length=20)
    expired_contract = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class HotTicket(models.Model):
    """
    Table: HotTickets
    Comment: The place to store all the Hot Tickets
    """
    ticket_id = models.BigIntegerField(null=False, unique=True)
    org_id = models.BigIntegerField(null=False, db_index=True)
    hot = models.BooleanField()

    def __str__(self):
        return self.ticket_id


class TicketNote(models.Model):
    """
    Table: TicketNotes
    Comment: The place to store all the ticketNotes
    """
    ticket_id = models.BigIntegerField(null=False, db_index=True)
    org_id = models.BigIntegerField(null=False, db_index=True)
    author = models.CharField(max_length=30, null=False, default="Unknown")
    created = models.DateTimeField(auto_now=True, null=False)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return str(self.ticket_id)

