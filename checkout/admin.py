from django.contrib import admin
from .models import Order, OrderLineItem
from products.models import Product

# Register your models here.


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
        )

    fields = (
        'order_number',
        'user_profile',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
        'order_shipped',
        )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'grand_total',
        'order_shipped',
    )

    ordering = ('-date',)

    # actions = ['delete_model']

    # def delete_model(self, request, obj):
    #     products = OrderLineItem.objects.get(request)
    #     for item in products():
    #         item += OrderLineItem.quantity
    #         obj.delete()


admin.site.register(Order, OrderAdmin)
