from . import views
from django.conf.urls import url
from .views import userprofile,taskstatus

urlpatterns=[
    url(r'^profile', userprofile,name='profile'),
    url(r'^statuschanger/(.*)$', taskstatus,name='statuschanger'),
    url(r'^$',views.homepage,name='homepage'),]


