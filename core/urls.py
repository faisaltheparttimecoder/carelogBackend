from django.conf.urls import url
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # Url to login and store the user information on the database
    url(r'^auth/google$', views.Login),

    # url to obtain the username of the connected user
    url(r'^connected_user/$', views.loggedUser.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
