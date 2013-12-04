from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from manager.models import Customer, Contact
from compiler.ast import TryExcept
from django.contrib.redirects.models import Redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

# index page, currently empty
# login_url_own = reverse('manager:login')

# @login_required(login_url = login_url_own)
class IndexView(TemplateView):
    template_name = 'manager/index.html'


 
#===============================================================================
# Customer related
#===============================================================================
class AllCustomersView(generic.ListView):
    template_name = 'manager/allcustomers.html'
    context_object_name = 'all_customers'
    
    def get_queryset(self):
        return Customer.objects.all()
      
class CustomerView(generic.DetailView):
    template_name = 'manager/customer.html'
    model = Customer
    
class NewCustomerView(generic.ListView):
    template_name = 'manager/newcustomer.html'
    model = Customer
    
def addCustomer(request):
    cus_name = request.POST['name']
    cus_address = request.POST['address']
    cus_info = request.POST['extrainfo']
    if(cus_name == "" or cus_address == "" or cus_info == ""):
        
        return render(request, 'manager/newcustomer.html', { 'error_message': 'Fill all fields!', })
    else:
        c = Customer(name=cus_name, address=cus_address, extrainfo=cus_info)
        c.save()
    
        return HttpResponseRedirect(reverse('manager:show_all'))

class editCustomerView(generic.DetailView):
    template_name = 'manager/editcustomer.html'
    model = Customer

def handleCustomerEdit(request, pk):
    customer = get_object_or_404(Customer,id=pk)
    cus_name = request.POST['name']
    cus_address = request.POST['address']
    cus_info = request.POST['extrainfo']
    if(cus_name == "" or cus_address == "" or cus_info == ""):
        return render(request, 'manager/editcustomer.html', { 'error_message': 'Fill all fields!', 'customer': customer,})
    else:
        customer.name = cus_name
        customer.address = cus_address
        customer.extrainfo = cus_info
        customer.save()
    
        return HttpResponseRedirect(reverse('manager:customerinfo', args=(customer.id,)))

def removeCustomer(request, cus_id):  
    customer = get_object_or_404(Customer, id=cus_id)
    customer.delete()
    
    return HttpResponseRedirect(reverse('manager:show_all'))      


#===============================================================================
# Contact related
#===============================================================================
class NewContactView(generic.ListView):
    template_name = 'manager/newcontact.html'
    context_object_name = 'all_customers'
    
    def get_queryset(self):
        return Customer.objects.all()

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
        return render(request, 'manager/newcontact.html', { 'error_message': 'Fill all fields!', 'all_customers': Customer.objects.all(),})
    else:
        # save data
        con = Contact(customer = con_customer, name = con_name, lastname = con_lastname, job = con_job, phone = con_phone, email = con_email)
        con.save()
        
        return HttpResponseRedirect(reverse('manager:customerinfo', args=(con_customer.id,)))
   
def editContactView(request, cus_id, con_id):
    template_name = 'manager/editcontact.html'
    customer = get_object_or_404(Customer, id=cus_id)
    contact = get_object_or_404(Contact, id=con_id)
    return render(request, template_name, {'customer': customer, 'contact': contact,})
     
def handleContactEdit(request, cus_id, con_id):
    customer = get_object_or_404(Customer, id=cus_id)
    contact = get_object_or_404(Contact, id=con_id)
    con_name = request.POST['name']
    con_lastname = request.POST['lastname']
    con_job = request.POST['job']
    con_phone = request.POST['phone']
    con_email = request.POST['email']
    
    if(con_name == "" or con_lastname == "" or con_job == "" or con_phone == "" or con_email == ""):
        return render(request, 'manager/editcontact.html', { 'error_message': 'Fill all fields!', 'customer': customer, 'contact': contact,})
    else:
        # save data
        contact.customer = customer
        contact.name = con_name
        contact.lastname = con_lastname
        contact.job = con_job
        contact.phone = con_phone
        contact.email = con_email
        
        contact.save()
        
        return HttpResponseRedirect(reverse('manager:customerinfo', args=(customer.id,)))

def removeContact(request, cus_id, con_id):
    contact = get_object_or_404(Contact, id=con_id)
    contact.delete()
    
    return HttpResponseRedirect(reverse('manager:customerinfo', args=(cus_id,)))


#===============================================================================
# Login related
#===============================================================================
class LoginView(generic.TemplateView):
    template_name = 'manager/login.html'
    
def handleLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # user & passw ok
            return HttpResponseRedirect(reverse('manager:show_all'))
        else:
            # user or passw wrong
            return HttpResponseRedirect(reverse('manager:login'))
    else:
        # user or passw wrong
        return HttpResponseRedirect(reverse('manager:login'))
     
def handleLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager:login'))
    