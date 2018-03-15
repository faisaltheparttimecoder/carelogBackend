from django.contrib import admin
from product.models import product


# Overriding the Django Default views.
class ProductAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of product app
    """
    list_display = ["name", "slug", "url"]

    class Meta:
        model = product


# Register all the tables on the Django website display
admin.site.register(product, ProductAdmin)