from django.conf.urls import patterns, url

from hallinta import views

urlpatterns = patterns('',
    # paasivulla kaikki asiakkaat
    url(r'^showall/$', views.IndexView.as_view(), name='show_all'),
    url(r'^specifics/(?P<pk>\d+)/$', views.CustomerView.as_view(), name='customerinfo'),
    url(r'^new/customer/$', views.NewCustomerView.as_view(), name='add_customer_form'),
    url(r'^new/customer/add/$', views.addCustomer, name='add_customer_new'),
    url(r'^new/contact/$', views.NewContactView.as_view(), name='add_contact_form'),
    url(r'^new/contact/add/$', views.addContact, name='add_contact_new'),
    # login at front page
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^login/handle/$', views.handleLogin, name='login_handle'),
    url(r'^logout/handle/$', views.handleLogout, name='logout_handle'),
)