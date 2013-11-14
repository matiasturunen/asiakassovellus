from django.db import models

class Asiakas(models.Model):
    nimi = models.CharField(max_length=200)
    osoite = models.CharField(max_length=200)
    lisatieto = models.TextField()
    
    #hiukan siistimpi nimi
    def __unicode__(self):
        return self.nimi
    
class Yhteyshenkilo(models.Model):
    asiakas = models.ForeignKey(Asiakas)
    nimi = models.CharField(max_length=200)
    sukunimi = models.CharField(max_length=200)
    tyonkuva = models.CharField(max_length=200)
    puh = models.CharField(max_length=40)
    email = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.sukunimi + ' ' + self.nimi
    