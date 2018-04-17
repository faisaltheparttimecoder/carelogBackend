from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from home import views

urlpatterns = [
    # Api URL, for the main timeline page
    url(r'^api/bcs/team/$', views.BcsTeamList.as_view()),
    url(r'^api/bcs/team/(?P<pk>[0-9]+)/$', views.BcsTeameDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)