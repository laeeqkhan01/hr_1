from django.conf import settings
from django.db   import models

# Create your models here.

class Worker(models.Model):
    name   = models.CharField(max_length=32)
    age    = models.IntegerField()
    dept   = models.CharField(max_length=16)
    salary = models.IntegerField()

    def gets_raise(self):
      self.salary *= 1.1

    def __str__(self):
      return self.name
    
