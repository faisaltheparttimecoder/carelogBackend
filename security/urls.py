from django.conf.urls import url
from . import views

urlpatterns = [

    # Security URL..
    url(r'^security/$', views.security, name="security"),

    # Security URL with args..
    url(r'^security/(?P<rssItem>\d+)/$', views.security, name="securityWithOptions"),

    # New source of RSS Feed
    url(r'^security/post/$', views.new_rss_feed, name="new_rss_feed"),

]