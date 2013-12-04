from django.db import models

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
    