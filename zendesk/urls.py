from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from zendesk import views

urlpatterns = [

    # Api URL, for the organization search
    url(r'^api/customer/search/(.*)/$', views.ZendeskSearch.as_view()),

    # API URL, to get the zendesk ticket comments
    url(r'^api/customer/comments/(?P<ticket>[0-9]+)/$', views.ZendeskTicketComments.as_view()),

    # API URL, to get the zendesk ticket metrics
    url(r'^api/customer/metrics/(?P<ticket>[0-9]+)/$', views.ZendeskTicketMetrics.as_view()),

    # Api URL, to load all the saved org
    url(r'^api/customer/organisation/$', views.OrganisationList.as_view()),
    url(r'^api/customer/organisation/(?P<pk>[0-9]+)/$', views.OrganisationDetails.as_view()),

    # Api URL, to load all the saved ticket notes
    url(r'^api/customer/ticketnotes/$', views.TicketNoteList.as_view()),
    url(r'^api/customer/ticketnotes/(?P<pk>[0-9]+)/$', views.TicketNoteDetails.as_view()),

    # Api URL, to load all the hot ticket
    url(r'^api/customer/hottickets/$', views.HotTicketsList.as_view()),
    url(r'^api/customer/hottickets/(?P<pk>[0-9]+)/$', views.HotTicketDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)