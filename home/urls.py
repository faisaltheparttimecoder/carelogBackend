from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from home import views

urlpatterns = [
    # Api URL, for the team page
    url(r'^api/bcs/team/$', views.BcsTeamList.as_view()),
    url(r'^api/bcs/team/(?P<pk>[0-9]+)/$', views.BcsTeamDetails.as_view()),

    # Api URL, for the main page
    url(r'^api/bcs/main/$', views.MainPageList.as_view()),
    url(r'^api/bcs/main/(?P<pk>[0-9]+)/$', views.MainPageDetails.as_view()),

    # Api URL, for the achievement page
    url(r'^api/bcs/certification/$', views.CertificationList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)