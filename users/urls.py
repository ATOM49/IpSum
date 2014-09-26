from django.conf.urls import patterns, url
from users import views
from core import views as core_views


urlpatterns = patterns('',
    url(r'^home/$', views.HomeView, name='home'),
    url(r'^editprofile/$', views.EditProfileView, name='editprofile'),

    url(r'^offers/$', views.OfferView, name='offers'),

    url(r'^findshops/$', views.FindShopsView, name='findshops'),
    url(r'^(?P<shopid>\d+)/$', views.ShopView, name='shopview'),
    url(r'^(?P<shopid>\d+/like_shop)/$', views.like_shop, name='like_shop'),

    url(r'^findproducts/$', views.FindProductsView, name='findproducts'),
    url(r'^allsellers/(?P<prodid>\d+)/$', views.AllSellersView, name='allsellers'),

    url(r'^points/$', views.PointsView, name='points'),

    url(r'^shoppingcart/$', views.ShoppingCartView, name='shoppingcart'),

    url(r'^nearbyshops/$', views.NearbyShopsView, name='nearbyshops'),
    url(r'^likedshops/$', views.LikedShopsView, name='likedshops'),
    url(r'^visitedshops/$', views.VisitedShopsView, name='visitedshops'),


    url(r'^logout/$', core_views.LogoutView, name='logout'),
)
