from django.contrib import admin
from resources.models import Resource


# Overriding the Django Default views.
class ResourceAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of links app
    """
    list_display = ["name", "updated"]

    class Meta:
        model = Resource


# Register all the tables on the Django website display
admin.site.register(Resource, ResourceAdmin)
