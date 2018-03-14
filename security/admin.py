from django.contrib import admin
from security.models import rssfeed


# Overriding the Django Default views.
class RssFeedAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of rssfeed app
    """
    list_display = ["feedname", "feedurl"]

    class Meta:
        model = rssfeed


# Register all the tables on the Django website display
admin.site.register(rssfeed, RssFeedAdmin)