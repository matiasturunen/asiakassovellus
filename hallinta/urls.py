from django.conf.urls import patterns, url

from hallinta import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/', views.AsiakasView.as_view(), name='asiakastieto'),
    url(r'^uusi/asiakas/', views.UusiAsiakasView.as_view(), name='lisaa_asiakas'),
)