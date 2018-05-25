from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from resources import views

urlpatterns = [

    # Api URL, for the main link page
    url(r'^api/resource/$', views.ResourceList.as_view()),

    # Api URL, for the links page for a particular ID.
    url(r'^api/resource/(?P<pk>[0-9]+)/$', views.ResourceDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)