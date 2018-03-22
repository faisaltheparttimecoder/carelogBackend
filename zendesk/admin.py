from django.contrib import admin
from zendesk.models import Organisation


# Overriding the Django Default views.
class OrganisationAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of rssfeed app
    """
    list_display = ["org_id", "name", "created_at", "location", "expired_contract"]

    class Meta:
        model = Organisation


# Register all the tables on the Django website display
admin.site.register(Organisation, OrganisationAdmin)