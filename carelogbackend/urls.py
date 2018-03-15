from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [

    # Admin Site
    url(r'^admin/', admin.site.urls),

    # All the URL from the Core app
    url(r'^', include('core.urls')),

    # All the URL from the Security app
    url(r'^', include('security.urls')),

    # All the URL from the Product app
    url(r'^', include('product.urls')),
]
