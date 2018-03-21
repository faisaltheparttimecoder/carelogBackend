from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from security import views

urlpatterns = [

    # Api URL, for the main security page
    url(r'^api/security/$', views.RssFeedList.as_view()),

    # Api URL, for the security page for a particular ID.
    url(r'^api/security/(?P<pk>[0-9]+)/$', views.RssFeedDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)