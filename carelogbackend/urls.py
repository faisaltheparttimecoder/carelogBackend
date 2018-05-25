from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [

    # The main admin page
    path('admin/', admin.site.urls),

    # Social Authentication URL
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),

    # All the core page URL
    url(r'^', include('core.urls')),

    # All the security page URL
    url(r'^', include('security.urls')),

    # All product page URL
    url(r'^', include('products.urls')),

    # All links page URL
    url(r'^', include('links.urls')),

    # All Resources page URL
    url(r'^', include('resources.urls')),

    # All zendesk page URL
    url(r'^', include('zendesk.urls')),

    # All timeline page URL
    url(r'^', include('timeline.urls')),

    # All Enviornment page URL
    url(r'^', include('environment.urls')),

    # All Home page URL
    url(r'^', include('home.urls')),
]
