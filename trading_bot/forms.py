from django import forms

from.models import Userresume#,User_stock_keys

class Resume(forms.ModelForm):
    class Meta:
        model = Userresume
        fields =(
            'name',
            'email',
            'reasone'
        )

# class User_stock_keys_form(forms.ModelForm):
#     class Mera:
#         model = User_stock_keys
#         fields = (
#             'api_key',
#             'api_secret',
#             'access_token'
#         )