from django.conf import settings
from django.db import models

class Cat(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    age = models.BigIntegerField()


class Dog(models.Model):
    name = models.CharField(max_length=256,)
    age = models.BigIntegerField()
class Alligator(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    age = models.BigIntegerField()
