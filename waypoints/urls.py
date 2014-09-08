# Import django modules
from django.conf.urls import url, patterns
from waypoints import views


urlpatterns = patterns('',
    url(r'^index/$', views.IndexView, name='index'),
    url(r'^save$', views.SaveView, name='save'),
    url(r'^search$', views.SearchView, name='search'),
    url(r'^upload$', views.UploadView, name='upload'),
)