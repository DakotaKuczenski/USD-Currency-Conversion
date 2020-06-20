from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.shortcuts import render , redirect
from .forms import HomeForm
from django.views.generic import TemplateView
import requests

class inputhome(TemplateView):
    template_name = 'currencyConversion/inputhome.html'

    def get(self, request, *args, **kwargs):

        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):

        form = HomeForm(request.POST)
        if form.is_valid():
            textamount = form.cleaned_data['amount']
            textto = form.cleaned_data['currency_to']



        url = 'http://api.currencylayer.com/live?access_key='

        r = requests.get(url).json()

        info = {
            'source' : r['source'],
            'to' : r['quotes']['USD' + textto]
        }

        x = info['to']
        result = float(x) * float(textamount)

        args = {'form': form, 'result': result }

        return render(request, self.template_name, args )
