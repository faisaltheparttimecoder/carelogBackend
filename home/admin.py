from django.contrib import admin
from home.models import BcsTeam, MainPage


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


class MainPageAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of MainPage app
    """
    list_display = [
        "page",
        "content",
    ]

    class Meta:
        model = MainPage


# Register all the tables on the Django website display
admin.site.register(BcsTeam, BcsTeamAdmin)