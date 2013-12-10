from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from manager.models import Customer, Contact, CustomerForm, ContactForm
from compiler.ast import TryExcept
from django.contrib.redirects.models import Redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.forms.models import modelformset_factory, modelform_factory
from django.forms import ModelForm, forms, formsets
from django.forms.formsets import formset_factory


# index page, currently empty

def IndexView(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/index.html'
    return render(request,template_name)


 
#===============================================================================
# Customer related
#===============================================================================
def AllCustomersView(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/allcustomers.html'   
    return render(request,template_name,{'all_customers': Customer.objects.all(), })
    
      
def CustomerView(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/customer.html'
    customer = get_object_or_404(Customer, id=pk)
    return render(request, template_name, {'customer': customer,})
    
def NewCustomerView(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/newcustomer.html'
    
    # empty form
    customer_form = CustomerForm
    
    if request.method == 'POST':
        form = customer_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:show_all'))
            
    else:
        form = customer_form
    
    return render(request, template_name, {'form': form, })
    
    


def editCustomerView(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/editcustomer.html'
    
    # get editable customer
    customer = get_object_or_404(Customer, id=pk)
    
    # empty form
    customer_form = CustomerForm

    if request.method == 'POST':
        form = customer_form(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('manager:customerinfo', args=(customer.id,)))
    
    else:
        form = customer_form(instance = customer)
          
    return render(request, template_name, {'form': form, })


def removeCustomer(request, cus_id):  
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    customer = get_object_or_404(Customer, id=cus_id)
    customer.delete()
    
    return HttpResponseRedirect(reverse('manager:show_all'))      


#===============================================================================
# Contact related
#===============================================================================
def NewContactView(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/newcontact.html'
    
    contact_form = ContactForm
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('manager:show_all'))
    else:
        form = contact_form()
        
    return render(request, template_name, {'form': form, })


 
def editContactView(request, cus_id, con_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    template_name = 'manager/editcontact.html'
    
    contact = get_object_or_404(Contact, id=con_id)
    
    contact_form = ContactForm
    if request.method == 'POST':
        form = contact_form(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('manager:customerinfo', args=(cus_id,)))
    else:
        form = contact_form(instance = contact)
        
    return render(request,template_name, {'form': form, 'contact': contact, })

     
def handleContactEdit(request, cus_id, con_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
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
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('manager:login'))
    
    contact = get_object_or_404(Contact, id=con_id)
    contact.delete()
    
    return HttpResponseRedirect(reverse('manager:customerinfo', args=(cus_id,)))


#===============================================================================
# Login related
#===============================================================================
def LoginView(request):
    template_name = 'manager/login.html'
    return render(request, template_name)
    
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

    