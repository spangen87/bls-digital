from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model for the product categories. The same as Boutique Ado Walkthrough.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for the products
    """
    class Meta:
        ordering = ('-name',)

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=254,
        unique=True,
        help_text='Full name including color if applicable.'
        )
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    weight_in_grams = models.IntegerField(
        null=True,
        blank=True,
        help_text='In grams. No decimals.'
        )
    price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField()
    origin = models.CharField(max_length=254, null=True, blank=True)
    document_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text='URL to manual or other file from manufacturer'
        )
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    quantity = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """
    Model for product reviews
    """
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    """
    Model for users to save their favoutite
    products to a wishlist
    """
    product = models.ForeignKey(
        Product, related_name='wishlist', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='wishlist', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
