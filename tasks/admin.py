from django.contrib import admin
from tasks.models import LastRun, BackupHistory


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


# Backup history site display
class BackupHistoryModelAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display for backup history table
    """
    list_display = [
        "backup_date",
        "backup_status",
        "backup_file",
        "backup_size_in_kb"
    ]

    class Meta:
        model = BackupHistory


# Register all tables to the admin site
admin.site.register(LastRun, lastRunModelAdmin)
admin.site.register(BackupHistory, BackupHistoryModelAdmin)
