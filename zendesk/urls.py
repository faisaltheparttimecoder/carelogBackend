

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from zendesk import views

urlpatterns = [

    # Api URL, for the organization search
    url(r'^api/zendesk/search/(.*)/$', views.ZendeskSearch.as_view()),

    # Api URL, to load all the saved org
    url(r'^api/zendesk/organisation/$', views.OrganisationList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)