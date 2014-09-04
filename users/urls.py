from django.conf.urls import patterns, url
from users import views
from core import views as core_views
urlpatterns = patterns('',
    url(r'^home/$', views.HomeView, name='home'),
    url(r'^offers/$', views.OfferView, name='offers'),

    url(r'^findshops/$', views.FindShopsView, name='findshops'),
    url(r'^(?P<shopid>\d+)/$', views.ShopView, name='shopview'),

    url(r'^findproducts/$', views.FindProductsView, name='findproducts'),
    url(r'^allsellers/(?P<prodid>\d+)/$', views.AllSellersView, name='allsellers'),

    url(r'^points/$', views.PointsView, name='points'),

    url(r'^logout/$', core_views.LogoutView, name='logout'),
    url(r'^shoppingcart/$', views.ShoppingCartView, name='shoppingcart'),
)