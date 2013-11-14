from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from hallinta.models import Asiakas

class IndexView(generic.ListView):
    template_name = 'hallinta/index.html'
    context_object_name = 'kaikki_asiakkaat'
    
    def get_queryset(self):
        return Asiakas.objects.all()
   
class AsiakasView(generic.DetailView):
    template_name = 'hallinta/asiakas.html'
    model = Asiakas
    
class UusiAsiakasView(generic.ListView):
    template_name = 'hallinta/uusiasiakas.html'
    model = Asiakas
    