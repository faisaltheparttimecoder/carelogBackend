from django.contrib import admin
from environment.models import AccountInformation, ContactInformation, EnvironmentNote


# Overriding the Django Default views.
class AccountInformationAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of AccountInformation Admin app
    """
    list_display = ["org_id", "info"]

    class Meta:
        model = AccountInformation


class ContactInformationAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of ContactInformation Admin app
    """
    list_display = ["org_id", "info"]

    class Meta:
        model = ContactInformation


class EnvironmentNotesAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of EnvironmentNotes Admin app
    """
    list_display = ["org_id", "title", "created", "updated",  "info"]

    class Meta:
        model = EnvironmentNote


# Register all the tables on the Django website display
admin.site.register(AccountInformation, AccountInformationAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(EnvironmentNote, EnvironmentNotesAdmin)
