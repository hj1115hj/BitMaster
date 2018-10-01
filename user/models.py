# Create your models here.
from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return 'user(%s, %s, %s, %s)' % (self.email, self.password, self.name, self.gender)
