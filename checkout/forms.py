from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update(
            {'pattern': '^\+\d{8,17}$'})
        self.fields['full_name'].widget.attrs.update(
            {'pattern':
                "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"})
        self.fields['street_address1'].widget.attrs.update(
            {'pattern':
                "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"})
        self.fields['town_or_city'].widget.attrs.update(
            {'pattern':
                "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"})

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
