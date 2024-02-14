from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    albumname = models.CharField(max_length=30)
    albumreleasedate = models.DateTimeField()
    rating= models.IntegerField()
    musician=  models.ForeignKey(Musician, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.albumname


