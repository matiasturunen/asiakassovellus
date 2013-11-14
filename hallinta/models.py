from django.db import models

class Asiakas(models.Model):
    nimi = models.CharField(max_lenght=200)
    osoite = models.CharField(max_lenght=200)
    lisatieto = models.TextField()
    
class Yhteyshenkilo(models.Model):
    asiakas = models.ForeignKey(Asiakas)
    nimi = models.CharField(max_lenght=200)
    sukunimi = models.CharField(max_lenght=200)
    tyonkuva = models.CharField(max_lenght=200)
    puh = models.CharField(max_lenght=40)
    email = models.CharField(max_lenght=200)
    