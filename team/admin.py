from django.contrib import admin
from team.models import BcsTeam


# Overriding the Django Default views.
class BcsTeamAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of BcsTeam app
    """
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "role",
        "region",
        "slack_handler"
    ]

    class Meta:
        model = BcsTeam


# Register all the tables on the Django website display
admin.site.register(BcsTeam, BcsTeamAdmin)