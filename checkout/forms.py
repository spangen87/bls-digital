from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'street_address1',
            'street_address2',
            'postcode',
            'town_or_city',
            'county',
            'country',
            'phone_number',
            'email',
            )
