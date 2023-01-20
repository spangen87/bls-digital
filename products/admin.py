from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.


class ProductReviewProductAdminInLine(admin.TabularInline):
    model = ProductReview


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductReviewProductAdminInLine,)

    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'image',
        'weight_in_grams',
        'origin',
        'quantity',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'stars',
        'content',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
