from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from products.forms import ProductForm
from shops.forms import ShopProfileForm, ShopAdminCatalogForm, \
    ShopAdminShopOfferForm, ShopAdminProductOfferForm
from shops.models import Catalog, Shop, ProductOffer, ShopOffer
from core.twilio_call import build_twilio_token


# Create your views here.

@login_required
def HomeView(request, shopid = None):
    context = {}
    shops = request.user.shop_set.all()
    context['shops'] = shops
    #check if shop if specified
    if shopid == None:
        if shops:
            shop = shops[0]
        else:
            shop = None
    #test that perms for specified shop exists
    else:
        try:
            shop = Shop.objects.get(id = shopid)
            if not shop.shop_admin.id == request.user.id:
                raise Exception
        except:
            return HttpResponse("The requested shop does not exist or is inaccessible for this current shopadmin.")



    #map_config
    change_location = False
    if request.method == 'POST':
        if 'update' in request.POST:
            change_location = True
        elif 'save' in request.POST:
            change_location = False
            shop.shop_latitude = request.POST['latitude']
            shop.shop_longitude = request.POST['longitude']
            shop.save()

    context["shop"] = shop
    context["change_location"] = change_location
    #print shop.shop_latitude, shop.shop_longitude
    return render_to_response("shops/shop_home.html", context, context_instance=RequestContext(request))


@login_required
def ManageCatalogView(request, shopid):
    if not request.user.groups.filter(name='shopadmin'):
        return HttpResponse("invalid group")
    template_name = "shops/manageCatalog.html"
    context = {}

    #check shop access perms
    try:
        shop = Shop.objects.get(id=shopid)
        if not shop.shop_admin.id == request.user.id:
            raise Exception
    except:
        return HttpResponse("The requested shop does not exist or is inaccessible for this current shopadmin.")

    product_form = None
    catalog_form = None

    context["shop"] = shop
    if request.method == 'POST':
        if request.GET.get("catalog_form") and int(request.GET.get("catalog_form")) == 2: #submitted
            print "catalog form submitted"
            catalog_form = ShopAdminCatalogForm(data=request.POST)
            if catalog_form.is_valid():
                catalog_item = catalog_form.save(commit = False)
                catalog_item.shop = shop
                catalog_item.save()
                print "catalog item saved"
                catalog_form = None
        elif request.GET.get("product_form") and int(request.GET.get("product_form")) == 2: #submitted
            print "product form submitted"
            product_form = ProductForm(data=request.POST)
            if product_form.is_valid():
                product_form.save()
                print "new product saved"
                product_form = None
    else:
        catalog_item_id_delete = request.GET.get("del")
        display_catalog_form = (request.GET.get("catalog_form"))
        display_product_form = (request.GET.get("product_form"))

        if catalog_item_id_delete:
            catalog_item = Catalog.objects.filter(id = catalog_item_id_delete)
            catalog_item.delete()
        if display_catalog_form:
            if int(display_catalog_form) == 1:
                catalog_form = ShopAdminCatalogForm()

        if display_product_form:
            if int(display_product_form) == 1:
                product_form = ProductForm()

        print catalog_item_id_delete
        print display_catalog_form
        print display_product_form

    context['catalog_form'] = catalog_form
    context['product_form'] = product_form

    #get list of shops owned
    catalog = shop.catalog_set.all()
    context['catalog'] = catalog

    #get list of shops owned
    shops = request.user.shop_set.all()
    context['shops'] = shops
    #shop ID part
    if shopid == None:
        shops = request.user.shop_set.all()
        if shops:
            shop = shops[0]
        else:
            shop = None
    #test that perms for specified shop exists
    else:
        try:
            shop = Shop.objects.get(id = shopid)
            if not shop.shop_admin.id == request.user.id:
                raise Exception
        except:
            return HttpResponse("The requested shop does not exist or is inaccessible for this current shopadmin.")

    context["shop"] = shop

    return render_to_response(template_name, context, context_instance=RequestContext(request))


@login_required
def ManageOffersView(request, shopid):
    if not request.user.groups.filter(name='shopadmin'):
        return HttpResponse("invalid group")

    template_name = "shops/manageOffers.html"
    context = {}

    #check shop access perms
    try:
        shop = Shop.objects.get(id = shopid)
        if not shop.shop_admin.id == request.user.id:
            raise Exception
    except:
        return HttpResponse("The requested shop does not exist or is inaccessible for this current shopadmin.")

    shop_offer_form = None
    product_offer_form = None

    context["shop"] = shop
    print shop

    if request.method == 'POST':
        if request.GET.get("shop_offer_form") and int(request.GET.get("shop_offer_form")) == 2: #submitted
            print "catalog form submitted"
            shop_offer_form = ShopAdminShopOfferForm(data=request.POST)
            if shop_offer_form.is_valid():
                shop_offer = shop_offer_form.save(commit = False)
                shop_offer.offer_shop = shop
                shop_offer.save()
                shop_offer_form = None
        elif request.GET.get("product_offer_form") and int(request.GET.get("product_offer_form")) == 2: #submitted
            product_offer_form = ShopAdminProductOfferForm(data=request.POST, shop=shop)
            if product_offer_form.is_valid():
                product = product_offer_form.cleaned_data.get('product')
                catalog_item = Catalog.objects.filter(shop_id=shop.id).get(product_id=product.id)
                product_offer = product_offer_form.save(commit = False)
                product_offer.offer_catalog_item = catalog_item
                product_offer.save()
                product_offer_form = None
    else:
        shop_offer_id_delete = request.GET.get("delshopoff")
        product_offer_id_delete = request.GET.get("delprodoff")
        display_shop_offer_form = (request.GET.get("shop_offer_form"))
        display_product_offer_form = (request.GET.get("product_offer_form"))

        if shop_offer_id_delete:
            shop_offer = ShopOffer.objects.filter(id = shop_offer_id_delete)
            shop_offer.delete()

        if product_offer_id_delete:
            product_offer = ProductOffer.objects.filter(id = product_offer_id_delete)
            product_offer.delete()

        if display_shop_offer_form:
            if int(display_shop_offer_form) == 1:
                shop_offer_form = ShopAdminShopOfferForm()

        if display_product_offer_form:
            if int(display_product_offer_form) == 1:
                product_offer_form = ShopAdminProductOfferForm(shop=shop)

    #print shop_offer_form
    context['shop_offer_form'] = shop_offer_form
    context['product_offer_form'] = product_offer_form


    #get list of shop offers
    shop_offers = shop.shopoffer_set.all()
    context['shop_offers'] = shop_offers

    #get list of product offers
    product_offers = ProductOffer.objects.filter(offer_catalog_item__shop_id=shop.id)
    context['shop_offers'] = shop_offers
    context['product_offers'] = product_offers

    #list of shops
    shops = request.user.shop_set.all()
    context['shops'] = shops
    #shop ID part
    if shopid == None:
        shops = request.user.shop_set.all()
        if shops:
            shop = shops[0]
        else:
            shop = None
    #test that perms for specified shop exists
    else:
        try:
            shop = Shop.objects.get(id = shopid)
            if not shop.shop_admin.id == request.user.id:
                raise Exception
        except:
            return HttpResponse("The requested shop does not exist or is inaccessible for this current shopadmin.")

    context["shop"] = shop

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
def ManageShopsView(request):
    if not request.user.groups.filter(name='shopadmin'):
        return HttpResponse("invalid group")
    context = {}
    if request.method == 'POST':
        shop_form = ShopProfileForm(data=request.POST)
        if shop_form.is_valid():
            shop = shop_form.save(commit=False)
            shop.shop_admin = request.user
            shop.save()
            shop_form = None

    else:
        shopid_delete = request.GET.get("del")
        display_shop_form = request.GET.get("shop_form")

        #
        if shopid_delete and int(shopid_delete) == 1:
            shop = Shop.objects.get(id = shopid_delete)
            shop.delete()
        print display_shop_form
        if display_shop_form and int(display_shop_form) == 1:
            shop_form = ShopProfileForm()
        else:
            shop_form = None

    context['shop_form'] = shop_form

    #get list of shops owned
    shops = request.user.shop_set.all()
    context['shops'] = shops
    return render_to_response("shops/manageShops.html", context, context_instance=RequestContext(request))

p_app_id='89743'
p_secret='ce2ddcccec20e0ecd5a3'

@login_required
def CallControlView(request, shopid):
    p_key = 'fc3f7ce5a53bc331ec26'
    shop = Shop.objects.get(id=shopid)
    call_admin = shop.shop_admin
    token = build_twilio_token(call_admin)
    return render_to_response("shops/control_call.html", {"token" : token,"client_name" : call_admin,
        "pusher_key" : p_key}, context_instance=RequestContext(request))