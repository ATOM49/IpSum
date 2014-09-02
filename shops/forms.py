from django import forms

from products.models import Product
from shops.models import Shop, Catalog, ShopOffer, ProductOffer


class ShopProfileForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('shop_name', 'shop_category', 'shop_address', 'shop_email')

class ShopAdminCatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('product', 'price')

class ShopAdminShopOfferForm(forms.ModelForm):
    class Meta:
        model = ShopOffer
        exclude = ('offer_shop',)

class ShopAdminProductOfferForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.shop = kwargs.pop("shop")
        super(ShopAdminProductOfferForm, self).__init__(*args, **kwargs)
        productList = [c.product.id for c in Catalog.objects.filter(shop_id=self.shop.id)]
        self.fields["product"] = forms.ModelChoiceField(queryset=Product.objects.filter(id__in = productList))

    class Meta:
        model = ProductOffer
        exclude = ('offer_catalog_item',)