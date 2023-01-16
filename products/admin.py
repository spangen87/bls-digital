from django.contrib import admin
from .models import Product, Category, PurchaseOrder

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'image',
        'weight_in_grams',
        'origin',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
        'date',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
