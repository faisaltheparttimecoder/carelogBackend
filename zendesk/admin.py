from django.contrib import admin
from zendesk.models import Organisation, TicketNote, HotTicket, Ticket, LastOrgTicketLoaderRun


# Overriding the Django Default views.
class OrganisationAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Organization app
    """
    list_display = ["org_id", "name", "created_at", "location", "expired_contract", "recently_added"]

    class Meta:
        model = Organisation


class HotTicketAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Ticket Notes app
    """
    list_display = ["ticket_id", "hot"]

    class Meta:
        model = HotTicket


class TicketNoteAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Ticket Notes app
    """
    list_display = ["ticket_id", "created", "notes"]

    class Meta:
        model = TicketNote


class TicketAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Ticket app
    """
    list_display = ["ticket_id", "org_id", "created", "updated", "priority",
                    "product_version", "product_component", "product_component_category", "iaas", "type"]

    class Meta:
        model = Ticket


class LastOrgTicketLoaderRunAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Ticket app
    """
    list_display = ["org_id", "last", "runtime", "success"]

    class Meta:
        model = LastOrgTicketLoaderRun


# Register all the tables on the Django website display
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(HotTicket, HotTicketAdmin)
admin.site.register(TicketNote, TicketNoteAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(LastOrgTicketLoaderRun, LastOrgTicketLoaderRunAdmin)
