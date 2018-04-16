from django.db import models


class Organisation(models.Model):
    """
    Table: Organisation
    Comment: The place to store all the Organization
    """
    org_id = models.BigIntegerField(null=False, unique=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    created_at = models.DateField()
    location = models.CharField(max_length=20, default='')
    expired_contract = models.BooleanField(default=False)
    country = models.CharField(max_length=100, null=False)
    recently_added = models.BooleanField(default=True)
    archived = models.BooleanField(default=True)
    archived_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """
    Table: Tickets
    Comments: The placeholder for all the tickets.
    """
    ticket_id = models.BigIntegerField(null=False, unique=True)
    org_id = models.ForeignKey(Organisation, related_name='tickets_org', on_delete=models.CASCADE)
    created = models.DateTimeField(null=False)
    updated = models.DateTimeField(null=False)
    priority = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=15)
    submitter = models.CharField(max_length=50, null=False)
    assignee = models.CharField(max_length=50, null=False)
    product = models.CharField(max_length=100)
    kb = models.CharField(max_length=100)
    resolution_code = models.CharField(max_length=100)
    defect = models.CharField(max_length=100)
    product_version = models.CharField(max_length=100)
    product_component = models.CharField(max_length=100)
    product_component_category = models.CharField(max_length=50)
    iaas = models.CharField(max_length=100)
    environment = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.ticket_id)


class LastOrgTicketLoaderRun(models.Model):
    """
    Table: LastTicketLoadRun
    Comments: Check when was the last used search query used to extract the data.
    """
    org_id = models.ForeignKey(Organisation, related_name='last_load_org_tickets', on_delete=models.CASCADE)
    last = models.DateTimeField(auto_now=True, null=False)
    success = models.BooleanField()
    runtime = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.org_id)


class HotTicket(models.Model):
    """
    Table: HotTickets
    Comment: The place to store all the Hot Tickets
    """
    ticket_id = models.BigIntegerField(null=False, unique=True)
    org_id = models.ForeignKey(Organisation, related_name='hot_ticket_org', on_delete=models.CASCADE)
    hot = models.BooleanField()

    def __str__(self):
        return str(self.ticket_id)


class TicketNote(models.Model):
    """
    Table: TicketNotes
    Comment: The place to store all the ticketNotes
    """
    ticket_id = models.BigIntegerField(null=False, db_index=True)
    org_id = models.ForeignKey(Organisation, related_name='org', on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=False, default="Unknown")
    created = models.DateTimeField(auto_now=True, null=False)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return str(self.ticket_id)

