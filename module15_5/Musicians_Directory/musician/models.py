from django.db import models

# Create your models here.
class Musician(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=35)
    phonenumber = models.CharField(max_length=11)
    instrumenttype = models.CharField(max_length=80)

    def __str__(self):
        return self.firstname