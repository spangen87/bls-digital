from django import forms
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(
            c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class UpdateStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['quantity']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = (
            'stars',
            'content',
        )
