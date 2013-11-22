from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from hallinta.models import Customer, Contact
from compiler.ast import TryExcept
from django.contrib.redirects.models import Redirect

from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'hallinta/index.html'

class AllCustomersView(generic.ListView):
    template_name = 'hallinta/allcustomers.html'
    context_object_name = 'all_customers'
    
    def get_queryset(self):
        return Customer.objects.all()
      
class CustomerView(generic.DetailView):
    template_name = 'hallinta/customer.html'
    model = Customer
    
class NewCustomerView(generic.ListView):
    template_name = 'hallinta/newcustomer.html'
    model = Customer
    
class NewContactView(generic.ListView):
    template_name = 'hallinta/newcontact.html'
    context_object_name = 'all_customers'
    
    def get_queryset(self):
        return Customer.objects.all()

class LoginView(generic.TemplateView):
    template_name = 'hallinta/login.html'
    
def addCustomer(request):
    cus_name = request.POST['name']
    cus_address = request.POST['address']
    cus_info = request.POST['extrainfo']
    if(cus_name == "" or cus_address == "" or cus_info == ""):
        
        return render(request, 'hallinta/newcustomer.html', { 'error_message': 'Fill all fields!', })
    else:
        c = Customer(name=cus_name, address=cus_address, extrainfo=cus_info)
        c.save()
    
        return HttpResponseRedirect(reverse('hallinta:show_all'))

    

def addContact(request):
    customer_id = request.POST['customer']
    con_name = request.POST['name']
    con_lastname = request.POST['lastname']
    con_job = request.POST['job']
    con_phone = request.POST['phone']
    con_email = request.POST['email']
    
    #get customer
    con_customer = Customer.objects.get(id=customer_id)
    
    if(con_name == "" or con_lastname == "" or con_job == "" or con_phone == "" or con_email == ""):
        return render(request, 'hallinta/newcontact.html', { 'error_message': 'Fill all fields!', 'all_customers': Customer.objects.all(),})
    else:
        # save data
        con = Contact(customer = con_customer, name = con_name, lastname = con_lastname, job = con_job, phone = con_phone, email = con_email)
        con.save()
        
        return HttpResponseRedirect(reverse('hallinta:show_all'))


def handleLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # user & passw ok
            return HttpResponseRedirect(reverse('hallinta:show_all'))
        else:
            # user or passw wrong
            return HttpResponseRedirect(reverse('hallinta:login'))
    else:
        # user or passw wrong
        return HttpResponseRedirect(reverse('hallinta:login'))
    
    
def handleLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hallinta:login'))
    