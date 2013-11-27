from django.conf.urls import patterns, url
from hallinta import views

urlpatterns = patterns('',
    # index page
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    # show all customers
    url(r'^showall/$', views.AllCustomersView.as_view(), name='show_all'),
    # show info from specific customer
    url(r'^customer/(?P<pk>\d+)/$', views.CustomerView.as_view(), name='customerinfo'),
    
    
    #===========================================================================
    # New customers and contacts
    #===========================================================================
    
    # show new customer view
    url(r'^new/customer/$', views.NewCustomerView.as_view(), name='add_customer_form'),
    # handle new customer adding
    url(r'^new/customer/add/$', views.addCustomer, name='add_customer_new'),
    # show new contact view
    url(r'^new/contact/$', views.NewContactView.as_view(), name='add_contact_form'),
    # handle new contact adding
    url(r'^new/contact/add/$', views.addContact, name='add_contact_new'),
    
    
    #===========================================================================
    # Data editing
    #===========================================================================
    
    # edit customer data
    url(r'^customer/(?P<pk>\d+)/edit/$', views.editCustomerView.as_view(), name='edit_customer_form'),
    # handle customer editing
    url(r'^customer/(?P<pk>\d+)/edit/handle$', views.handleCustomerEdit, name='edit_customer_handle'),
    # edit contact data
    url(r'^customer/(?P<cus_id>\d+)/contact/(?P<con_id>\d+)/edit/$', views.editContactView, name='edit_contact_form'),
    # handle contact editing
    url(r'^customer/(?P<cus_id>\d+)/contact/(?P<con_id>\d+)/edit/handle$', views.handleContactEdit, name='edit_contact_handle'),
    
    
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
    url(r'^$', views.LoginView.as_view(), name='login'),
    # handle login
    url(r'^login/handle/$', views.handleLogin, name='login_handle'),
    # handle logout
    url(r'^logout/handle/$', views.handleLogout, name='logout_handle'),
)