from django.contrib import admin
from environment.models import AccountInformation


# Overriding the Django Default views.
class AccountInformationAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of TimelineAdmin app
    """
    list_display = ["org_id", "info"]

    class Meta:
        model = AccountInformation


# Register all the tables on the Django website display
admin.site.register(AccountInformation, AccountInformationAdmin)

