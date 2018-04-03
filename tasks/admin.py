from django.contrib import admin
from tasks.models import LastRun

# Last Run site display
class lastRunModelAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display for backup history table
    """
    list_display = [
        "component",
        "last_run"
    ]

    class Meta:
        model = LastRun


# Register all tables to the admin site
admin.site.register(LastRun, lastRunModelAdmin)
