from django.contrib import admin
from links.models import Category, Link


# Overriding the Django Default views.
class CategoryAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of links app
    """
    list_display = ["name"]

    class Meta:
        model = Category


class LinkAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of links app
    """
    list_display = ["name", "url", "info"]

    class Meta:
        model = Link


# Register all the tables on the Django website display
admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
