from django.db import models

# Create your models here.

class PracticeModel(models.Model):
   
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    date = models.DateField()
    datetimefield = models.DateTimeField()
    decimalfield = models.DecimalField(max_digits=20, decimal_places=4)
    durationfield = models.DurationField()
    file = models.FileField()
    ip_address = models.GenericIPAddressField()
    image = models.ImageField()
    json = models.JSONField()
    positive_integer_big = models.PositiveIntegerField()
    small_integer = models.PositiveSmallIntegerField()
    Slugfield = models.SlugField()
    uuid = models.UUIDField()
    agree = models.BooleanField(default=False)


