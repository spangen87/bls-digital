from django.contrib import admin
from .models import Product, Category, PurchaseOrder, ProductReview

# Register your models here.


class OrderPurchaseOrderAdminInLine(admin.TabularInline):
    model = PurchaseOrder
    readonly_fields = ('quantity',)


class ProductReviewProductAdminInLine(admin.TabularInline):
    model = ProductReview


class ProductAdmin(admin.ModelAdmin):
    inlines = (
        OrderPurchaseOrderAdminInLine,
        ProductReviewProductAdminInLine
        )

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


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'stars',
        'content',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
