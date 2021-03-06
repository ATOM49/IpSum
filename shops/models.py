from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from core import modelFieldChoicesManager as MCM
# from django.contrib.gis.db import models

# Create your models here.


class Zipcode(models.Model):
    code = models.IntegerField(max_length=6)
    # poly = models.PolygonField()
    # objects = models.GeoManager()

class Shop(models.Model):
    #Shop Details
    shop_name = models.CharField(max_length=128)
    shop_category = models.CharField(max_length=2,choices = MCM.SHOP_CATEGORY_CHOICES(), default = 'GS')

    #Shop Address
    shop_latitude = models.FloatField(max_length=20, null = True)
    shop_longitude = models.FloatField(max_length=20, null = True)
    shop_contact_no = models.CharField(max_length=15, null = True) # TODO multiple nos
    plot_num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices = MCM.STATE_CATEGORY_CHOICES())
    zipcode = models.IntegerField(max_length=6)


    #Shop Info
    #shop_image_path = models.FilePathField(null = True) # TODO change to store paths only
    shop_info_text = models.CharField(max_length=2048, null=True)#TODO change to hold file
    shop_facebookpage = models.CharField(max_length=100, null=True)
    shop_email = models.EmailField(max_length=30, null=True) # TODO multiple emails
    user_likes = models.IntegerField(null=True)
    user_visits = models.IntegerField(null=True)


    #Shop Admin
    shop_admin = models.ForeignKey(User)

    def __str__(self):
        return self.shop_name

    def get_address(self):
        shop_address = str(self.plot_num) + ", \n" + self.street +", \n"+ self.city+ ", \n" + self.state+", \n" + str(self.zipcode)
        return shop_address


class Catalog(models.Model):

    shop = models.ForeignKey(Shop)
    product = models.ForeignKey(Product)
    price = models.IntegerField(null = True)

    def __str__(self):
        return str(self.product)


class ProductOffer(models.Model):
    offer_name = models.CharField(max_length=128)
    offer_info = models.CharField(max_length=1024, null = True)
    points_needed = models.IntegerField(default = 0)#TODO make this flexible
    offer_catalog_item = models.ForeignKey(Catalog, null = True)
    is_eligible = False
    offer_added = models.DateField(auto_now=True)
    offer_To = models.DateField()
    offer_From = models.DateField()


    def eligibilityCheck(self, user, shop):
        relation, created = ShopUserRelation.objects.get_or_create(user_id=user.id, shop_id=shop.id)
        points = relation.loyalty_points
        if self.points_needed > points:
            self.is_eligible = False
        else:
            self.is_eligible = True

    def __str__(self):
        return self.offer_name

    def ActiveOffers(self):
        now = models.DateTimeField(auto_now=True)
        if self.offer_To <= now <= self.offer_From:
            self.active = True


class ShopUserRelation(models.Model):

    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(User)

    shop_review = models.CharField(max_length=2048, blank=True)

    loyalty_points = models.IntegerField(default = 0)

    user_like = models.BooleanField(default = False)
    visited = models.BooleanField(default = False)


    def __str__(self):
        return "Shop User Relation Item " + str(self.id)


class ShopOffer(models.Model):
    offer_Name = models.CharField(max_length=128)
    offer_Info = models.CharField(max_length=1024, null = True)
    points_Needed = models.IntegerField(default = 0)#TODO make this flexible
    offer_Category = models.CharField(max_length=5 ,choices = MCM.PRODUCT_CATEGORY_CHOICES())
    offer_Shop = models.ForeignKey(Shop, null = True)
    is_eligible = False
    offer_added = models.DateField(auto_now=True)
    offer_From = models.DateField()
    offer_To = models.DateField()

    def eligibilityCheck(self, user):
        relation, created = ShopUserRelation.objects.get_or_create(user_id=user.id, shop_id=self.offer_shop.id)
        points = relation.loyalty_points
        if self.points_needed > points:
            self.is_eligible = False
        else:
            self.is_eligible = True

    def __str__(self):
        return self.offer_name

    def ActiveOffers(self):
        now = models.DateTimeField(auto_now=True)
        if self.offer_To <= now <= self.offer_From:
            self.active = True


class ProductUserRelation(models.Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    product_review = models.CharField(max_length=2048)

    def __str__(self):
        return "Product User Relation Item " + str(self.id)


class ShoppingCart(models.Model):

    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    shop = models.ForeignKey(Shop, null = True, default = None)
    isCatalogItem = False


class History(models.Model):

    date = models.DateField()
    product = models.ForeignKey(Product)
    #offer_availed = models.ForeignKey(Offer, null = True)#TODO multiple
    shop_user_relation = models.ForeignKey(ShopUserRelation)

    def __str__(self):
        return "History Item " + str(self.id)