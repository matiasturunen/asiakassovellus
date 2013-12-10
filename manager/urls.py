from django.conf.urls import patterns, url
from manager import views

urlpatterns = patterns('',
    # index page
    url(r'^index/$', views.IndexView, name='index'),
    # show all customers
    url(r'^showall/$', views.AllCustomersView, name='show_all'),
    # show info from specific customer
    url(r'^customer/(?P<pk>\d+)/$', views.CustomerView, name='customerinfo'),
    
    
    #===========================================================================
    # New customers and contacts
    #===========================================================================
    
    # show new customer view
    url(r'^customer/new/$', views.NewCustomerView, name='add_customer_form'),
    # show new contact view
    url(r'^contact/new/$', views.NewContactView, name='add_contact_form'),
    
    
    #===========================================================================
    # Data editing
    #===========================================================================
    
    # edit customer data
    url(r'^customer/(?P<pk>\d+)/edit/$', views.editCustomerView, name='edit_customer_form'),
    # edit contact data
    url(r'^customer/(?P<cus_id>\d+)/contact/(?P<con_id>\d+)/edit/$', views.editContactView, name='edit_contact_form'),
       
    
    #===========================================================================
    # removing
    #===========================================================================
    
    # remove customer
    url(r'^customer/(?P<cus_id>\d+)/remove/$', views.removeCustomer, name='customer_remove'),
    # remove contact
    url(r'^customer/(?P<cus_id>\d+)/contact/(?P<con_id>\d+)/remove/$', views.removeContact, name='contact_remove'),
    
    
    #===========================================================================
    # Login
    #===========================================================================
    
    # login at front page
    url(r'^$', views.LoginView, name='login'),
    # handle login
    url(r'^login/handle/$', views.handleLogin, name='login_handle'),
    # handle logout
    url(r'^logout/handle/$', views.handleLogout, name='logout_handle'),
)