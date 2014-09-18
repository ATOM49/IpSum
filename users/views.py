from datetime import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader

from products.models import Product
from shops.models import Shop, Catalog, ShopUserRelation, ProductOffer,\
    ShoppingCart
from users.models import UserProfile
from shops.views import HomeView as ShopAdminHomeView




@login_required
def HomeView(request,shopid=None):
    home=True
#Consumer Home
    if request.user.groups.filter(name='consumer'):
        visits = int(request.COOKIES.get('visits', '0'))
        if request.session.get('last_visit'):
            last_visit_time = request.session.get('last_visit')
            visits = request.session.get('visits', 0)
            if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).seconds > 7:
                request.session['visits'] = visits + 1
                request.session['last_visit'] = str(datetime.now())
        else:
            request.session['last_visit'] = str(datetime.now())
            request.session['visits'] = 1
        if request.session.get('visits'):
                count = request.session.get('visits')
        else:
            count = 0
        return render_to_response("user/home.html", {'visits':count,'home':home}, context_instance=RequestContext(request))

#Shop_Admin View
    elif request.user.groups.filter(name='shopadmin'):
        return ShopAdminHomeView(request, shopid)


    elif request.user.groups.filter(name='admin'):
        return HttpResponse("admin_home")


    else:
        return HttpResponse("invalid group")


@login_required
def FindShopsView(request):
    template_name = 'user/findShops.html'
    context_object_names = ['shop_list', 'queryString']
    if request.method == 'POST':
        queryString = request.POST['querystring']
        shopList = Shop.objects.filter(shop_name__contains=queryString)
        context_objects = [shopList, queryString]
    else:
        queryString = ''
        shopList = Shop.objects.all()
        context_objects = [shopList, queryString]
    context = dict(zip(context_object_names, context_objects))
    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
def ShopView(request, shopid):
    template_name = 'user/shop_view.html'
    context_objects_name = ('shop',
                            'shop_catalog',
                            'shop_offers',
                            'product_offers',
                            'shop_visited',
                            'shop_liked',
                            'loyalty_points',
                            'token')

    shop = Shop.objects.get(id=shopid)
    user = request.user
    relation,created = ShopUserRelation.objects.get_or_create(shop=shop,user=user)

    if request.GET.get('like'):
        if not relation.user_like:
            relation.user_like = True
            relation.loyalty_points += 50
            relation.save()
    if request.GET.get('visited'):
        if not relation.visited:
            relation.visited = True
            relation.loyalty_points += 100
            relation.save()
    if request.GET.get('cart'):
        itemid = int(request.GET.get('cart'))
        catalog_item = Catalog.objects.get(id=itemid)
        cart, created = ShoppingCart.objects.get_or_create(user=user, product=catalog_item.product, shop=catalog_item.shop)
        if not created:
            cart.isCatalogItem = True
            cart.save()
        #handle already in cart case using "created"
    print ShoppingCart.objects.all()

    #get list of shop offers
    shop_offers = shop.shopoffer_set.all()
    for offer in shop_offers: offer.eligibilityCheck(user)
    print shop_offers

    #get list of product offers
    product_offers = ProductOffer.objects.filter(offer_catalog_item__shop_id=shop.id)
    for offer in product_offers: offer.eligibilityCheck(user, shop)

    print relation.visited, relation.user_like, relation.loyalty_points

    token = build_twilio_token(user)

    context_objects = (shop,
                       shop.catalog_set.all(),
                       shop_offers,
                       product_offers,
                       relation.visited,
                       relation.user_like,
                       relation.loyalty_points,
                       token)
    context = RequestContext(request, dict(zip(context_objects_name, context_objects)))

    template = loader.get_template(template_name)
    return HttpResponse(template.render(context))

#for calls
def build_twilio_token(client_name):
 
    # Find these values at twilio.com/user/account
    account_sid = 'AC9dbcad82b20275e6e1854351444f13c3'
    auth_token = 'd5eb94487e911314e5620b4ea18e6d74'
 
    capability = TwilioCapability(account_sid, auth_token)
    # This is the app Sid of your TwiML app
    app_sid = 'AP4679912e15024febe5d6d1fc814e7c7d'
 
    capability.allow_client_outgoing(app_sid)
    capability.allow_client_incoming(client_name)
 
    return capability.generate()

@login_required
def FindProductsView(request):
    template_name = 'user/findProducts.html'
    context_object_names = ['product_list', 'queryString']
    if request.method == 'POST':
        queryString = request.POST['querystring']
        productList = Product.objects.filter(product_name__contains=queryString)
        context_objects = [productList, queryString]
    else:
        queryString = ''
        productList = Product.objects.all()
        context_objects = [productList, queryString]

    if request.GET.get('cart'):
        itemid = int(request.GET.get('cart'))
        product_item = Product.objects.get(id=itemid)
        cart, created = ShoppingCart.objects.get_or_create(user=request.user, product=product_item)
        if not created:
            cart.isCatalogItem = False
            cart.save()
        #handle already in cart case using "created"

    context = dict(zip(context_object_names, context_objects))
    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
def AllSellersView(request, prodid):
    template_name = 'user/allSellers.html'
    context_objects_name = ('catalogItems', 'product')
    p = Product.objects.get(id=prodid)
    catalogItems = p.catalog_set.all()
    context_objects = (catalogItems, p)
    context = RequestContext(request, dict(zip(context_objects_name,context_objects)))
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context))



@login_required
def OfferView(request):

    context= RequestContext(request)
    context = {"SiteOffers" : None}

    #shopOffers
    shops = Shop.objects.all()
    ShopOffers = []
    for s in shops:
        offers = s.shopoffer_set.all()
        if offers:
            for offer in offers:
                offer.eligibilityCheck(request.user)
                ShopOffers.append(offer)
    context["ShopOffers"] = ShopOffers

    #productOffers
    ProductOffers = []
    catalog_items = Catalog.objects.all()
    for c in catalog_items:
        offers = c.productoffer_set.all()
        if offers:
            for offer in offers:
                offer.eligibilityCheck(request.user, c.shop)
                ProductOffers.append(offer)
    context["ProductOffers"] = ProductOffers

    return render_to_response("user/offers.html",context,context_instance=RequestContext(request))


@login_required
def ShoppingCartView(request):
    shopping_cart = request.user.shoppingcart_set.all()
    context = {'shopping_cart' : shopping_cart}
    return render_to_response("user/shoppingCart.html",context,context_instance=RequestContext(request))

@login_required
def PointsView(request):
    user=request.user
    relations = request.user.shopuserrelation_set.all()
    context = {}
    context['relations'] = relations
    agg = request.user.shopuserrelation_set.aggregate(Sum("loyalty_points"))
    points = agg['loyalty_points__sum']
    if not points:
        points = 0
    context["loyalty_points"] = points
    print points
    return render_to_response("user/points.html",context,context_instance=RequestContext(request))
