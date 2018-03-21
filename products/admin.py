from django.contrib import admin
from products.models import Product


# Overriding the Django Default views.
class ProductAdmin(admin.ModelAdmin):
    """
    Override the default Django Admin website display of product app
    """
    list_display = ["name", "slug", "url"]

    class Meta:
        model = Product


# Register all the tables on the Django website display
admin.site.register(Product, ProductAdmin)