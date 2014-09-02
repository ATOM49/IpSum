from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^index/$', views.IndexView, name='index'),
    url(r'^register/(?P<usertype>[a-z]+)/$', views.RegistrationView, name='register'),
    url(r'^login/$', views.LoginView, name='login'),
   )