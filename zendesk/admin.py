from django.contrib import admin
from zendesk.models import Organisation, TicketNote, HotTicket


# Overriding the Django Default views.
class OrganisationAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Organization app
    """
    list_display = ["org_id", "name", "created_at", "location", "expired_contract"]

    class Meta:
        model = Organisation


class HotTicketAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Ticket Notes app
    """
    list_display = ["ticket_id", "org_id", "hot"]

    class Meta:
        model = HotTicket


class TicketNoteAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Ticket Notes app
    """
    list_display = ["ticket_id",  "org_id", "created", "notes"]

    class Meta:
        model = TicketNote


# Register all the tables on the Django website display
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(HotTicket, HotTicketAdmin)
admin.site.register(TicketNote, TicketNoteAdmin)