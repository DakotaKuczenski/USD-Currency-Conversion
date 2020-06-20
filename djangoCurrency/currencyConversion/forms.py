from django import forms


COUNTRY_CHOICES= [
    ('MXN', 'MXN'),
    ('RUB', 'RUB'),
    ('EUR', 'EUR'),
    ('CAD', 'CAD')
    ]

class HomeForm(forms.Form):
    amount = forms.DecimalField(required = True)
    currency_to = forms.CharField(required = True, widget=forms.Select(choices=COUNTRY_CHOICES))

