from django import forms


class OrderCreatedForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_adress = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()
