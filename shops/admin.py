from django.contrib import admin

from shops.models import Shop, History, ShopOffer, ProductOffer, Catalog, ShopUserRelation

# Register your models here.
class ShopOfferInline(admin.TabularInline):
    model = ShopOffer
    extra = 1

class CatalogInline(admin.TabularInline):
    model = Catalog
    extra = 1

class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'shop_email', 'shop_category', 'shop_info_text', 'shop_admin')
    inlines = [CatalogInline, ShopOfferInline]

class ProductOfferInline(admin.TabularInline):
    model = ProductOffer
    extra = 1

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('shop', 'product', 'price')
    inlines = [ProductOfferInline,]

admin.site.register(Shop, ShopAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(History)
admin.site.register(ShopUserRelation)