from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, Select

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    extrainfo = models.TextField()
    
    # better name
    def __unicode__(self):
        return self.name
    
class Contact(models.Model):
    customer = models.ForeignKey(Customer)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.lastname + ' ' + self.name

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'extrainfo')
        labels = {
            'name': ('Name'),
            'address': ('Address'),
            'extrainfo': ('Additional details'),
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'extrainfo': Textarea(attrs={'class': 'form-control'}),
        }
        
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('customer', 'name', 'lastname', 'job', 'phone', 'email')
        labels = {
            'customer': ('Customer'),
            'name': ('First name'),
            'lastname': ('Last name'),
            'job': ('Job description'),
            'phone': ('Phone'),
            'email': ('E-mail'),
            
        }
        widgets = {
            'customer': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'lastname': TextInput(attrs={'class': 'form-control'}),
            'job': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }
        