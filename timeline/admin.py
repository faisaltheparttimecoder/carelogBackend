from django.contrib import admin
from timeline.models import Timeline, TimelineDetail, TimelineCategory


# Overriding the Django Default views.
class TimelineAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of TimelineAdmin app
    """
    list_display = ["title", "description", "created"]

    class Meta:
        model = Timeline


class TimelineCategoryAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Timeline Category Table
    """
    list_display = ["name", "color", "icon"]

    class Meta:
        model = TimelineCategory


class TimelineDetailsAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of Timeline Details Table
    """
    list_display = ["title", "description", "timeline_id"]

    class Meta:
        model = TimelineDetail


# Register all the tables on the Django website display
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(TimelineCategory, TimelineCategoryAdmin)
admin.site.register(TimelineDetail, TimelineDetailsAdmin)