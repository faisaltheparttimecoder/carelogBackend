from django.contrib import admin
from security.models import RssFeed


# Overriding the Django Default views.
class RssFeedAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of rssfeed app
    """
    list_display = ["name", "url"]

    class Meta:
        model = RssFeed


# Register all the tables on the Django website display
admin.site.register(RssFeed, RssFeedAdmin)