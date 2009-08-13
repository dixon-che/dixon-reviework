'''Here activate admin for Person model'''

from django.contrib import admin
from basesite.Person.models import Person

admin.site.register(Person)
