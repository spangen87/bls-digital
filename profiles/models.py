from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User model for saving order history and default
    shipping information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+\d{8,17}$',
        message="Phone number must be entered in the format:\
             '+999999999'. Up to 15 digits allowed.")
    default_phone_number = models.CharField(
        validators=[phone_regex], max_length=18, blank=True, null=True,
        help_text='Phone number must be in the format +991112223')
    default_country = CountryField(null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Just save for existing users
    instance.userprofile.save()
