from django.conf.urls import url

from shops import views
from users import views as user_views
from core import views as core_views

urlpatterns = [
    url(r'^home(/(?P<shopid>\d+))?/$', user_views.HomeView, name='home'),
    url(r'^catalog/(?P<shopid>\d+)/', views.ManageCatalogView, name='managecatalog'),
    url(r'^offers/(?P<shopid>\d+)/', views.ManageOffersView, name='manageoffers'),
    url(r'^manageshops/', views.ManageShopsView, name='manageshops'),
    url(r'^logout/$', core_views.LogoutView, name='logout'),
]