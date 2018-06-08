# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name= models.CharField(max_length=101)
    city= models.CharField(max_length=101)
    state= models.CharField(max_length=101)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Ninjas(models.Model):
    first_name=models.CharField(max_length=101)
    last_name=models.CharField(max_length=101)
    dojo= models.ForeignKey(Dojo, related_name='ninjas')
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
