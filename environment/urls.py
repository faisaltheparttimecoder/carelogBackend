from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from environment import views

urlpatterns = [

    # Api URL, for the main account information page
    url(r'^api/customer/environment/account_info/$', views.AccountInformationList.as_view()),
    url(r'^api/customer/environment/account_info/(?P<pk>[0-9]+)/$', views.AccountInformationDetails.as_view()),

    # Api URL, for the main contact information page
    url(r'^api/customer/environment/contact_info/$', views.ContactInformationList.as_view()),
    url(r'^api/customer/environment/contact_info/(?P<pk>[0-9]+)/$', views.ContactInformationDetails.as_view()),

    # Api URL, for the main environment notes page
    url(r'^api/customer/environment/environment_notes/$', views.EnvironmentNotesList.as_view()),
    url(r'^api/customer/environment/environment_notes/(?P<pk>[0-9]+)/$', views.EnvironmentNotesDetails.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)