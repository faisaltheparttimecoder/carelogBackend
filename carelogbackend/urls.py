from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [

    # The main admin page
    path('admin/', admin.site.urls),

    # All the security page URL
    url(r'^', include('security.urls')),

    # All product page URL
    url(r'^', include('products.urls')),

    # All links page URL
    url(r'^', include('links.urls')),

    # All zendesk page URL
    url(r'^', include('zendesk.urls')),
]
