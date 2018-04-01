from django.conf.urls import url
from core import views

urlpatterns = [
    # Url to login and store the user information on the database
    url(r'^auth/google$', views.Login),
]
