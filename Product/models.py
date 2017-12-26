# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=10)
    Description = models.CharField(max_length=30)
    Price = models.IntegerField()
    InStock = models.BooleanField()

