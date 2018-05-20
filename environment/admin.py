from django.contrib import admin
from environment.models import AccountInformation, ContactInformation, EnvironmentNote, EnvironmentProductsList
from environment.models import EnvironmentType, EnvironmentInstanceProduct, EnvironmentInstance


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
    list_display = ["org_id", "title", "created", "updated",  "description"]

    class Meta:
        model = EnvironmentNote


class EnvironmentProductListAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of EnvironmentNotes Admin app
    """
    list_display = ["org_id"]

    class Meta:
        model = EnvironmentProductsList


class EnvironmentTypeAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of EnvironmentNotes Admin app
    """
    list_display = ["type"]

    class Meta:
        model = EnvironmentType


class EnvironmentInstanceAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of EnvironmentInstance Admin app
    """
    list_display = ["type_id", "org_id", "name", "infrastructure", "timeline_id"]

    class Meta:
        model = EnvironmentInstance


class EnvironmentInstanceProductAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of EnvironmentInstanceProducts Admin app
    """
    list_display = ["instance_id", "name", "version"]

    class Meta:
        model = EnvironmentInstanceProduct


# Register all the tables on the Django website display
admin.site.register(AccountInformation, AccountInformationAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(EnvironmentNote, EnvironmentNotesAdmin)
admin.site.register(EnvironmentProductsList, EnvironmentProductListAdmin)
admin.site.register(EnvironmentType, EnvironmentTypeAdmin)
admin.site.register(EnvironmentInstance, EnvironmentInstanceAdmin)
admin.site.register(EnvironmentInstanceProduct, EnvironmentInstanceProductAdmin)
