from django import forms
from products.models import Product
from shops.models import Shop, Catalog, ShopOffer, ProductOffer
# from localflavor.in_.forms import INPhoneNumberField, INZipCodeField
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class ShopProfileForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('shop_name',
                  'shop_category',
                  'shop_contact_no',
                  'shop_email',
                  'shop_facebookpage',
                  'plot_num',
                  'street',
                  'city',
                  'state',
                  'zipcode',
                 )

        labels = {
            'plot_num': _('Plot Num/House No'),
            'street': _('Street/Apartment')
        }
        widgets = {
            # 'shop_contact_no': INPhoneNumberField(),
            # 'zipcode': INZipCodeField()
        }

    def __init__(self):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Shop details',
                'shop_name',
                'shop_category',
                'username',
                'shop_email',
                'shop_facebookpage'
            ),
            Fieldset(
                'Address',
                'plot_no',
                'street',
                'city',
                'state',
                'zipcode'
            )
            )
        super(ShopProfileForm, self).__init__()


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