from django import forms
from .models import UserProfile
from phonenumber_field.formfields import PhoneNumberField


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
