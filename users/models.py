from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models import signals
from shops.models import Shop
from django.dispatch.dispatcher import receiver
# from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from core import modelFieldChoicesManager as MCM
from IpSum import settings
# Create your models here.

# class CustomFacebookModel(FacebookModel):
#     pass


class UserProfile(models.Model):
    avatar = models.ImageField("Profile Pic", upload_to="media/profile_pictures/", blank=True, null=True)
    user = models.OneToOneField(User, unique=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    plot_num = models.IntegerField(null=True)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=2, choices=MCM.STATE_CATEGORY_CHOICES(), null=True)
    zipcode = models.IntegerField(max_length=6, null=True)

    def __unicode__(self):
        return self.User.username


def create_profile(sender, instance, created, **kwargs):
    """Create a user profile when a new user account is created"""
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_profile, sender=User)


# class FacebookProfile(FacebookModel):
#     Fbuser = models.OneToOneField(CustomFacebookModel)
#
#     @receiver(post_save)
#     def create_profile(sender, instance, created, **kwargs):
#         if sender == get_user_model():
#             Fbuser = instance
#             profile_model = get_profile_model()
#             if profile_model == FacebookProfile and created:
#                 profile, new = FacebookProfile.objects.get_or_create(user=instance)