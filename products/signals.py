from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Product
from checkout.models import Order


@receiver(pre_delete, sender=Order)
def return_stock(sender, instance, **kwargs):
    """
    Add stock back to the inventory when an order is deleted
    """
    order_line_items = instance.lineitems.all()
    for item in order_line_items:
        product = Product.objects.get(pk=item.product.pk)
        product.quantity += item.quantity
        product.save()
