'''This model store info about person'''

from django.db import models


class Person(models.Model):
    '''Persons info'''

    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    date_of_birthday = models.DateField()
    email = models.EmailField(unique=True, max_length=64)
    cell_phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    curriculum_vita = models.TextField()
