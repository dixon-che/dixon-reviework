"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from basesite.Person.models import Person
from django.contrib.auth.models import User
import datetime
# class LentaTest(TestCase):
#     def test_index(self):
#         response = self.client.get('/lenta/')
#         self.failUnlessEqual(response.status_code, 200)


# Unit tests for every new Django model looks like:
# create/edit/delete object of the model
# call unicode() and get_absolute_url() methods
class SimpleTest(TestCase):
    user = None
    def test_basic_configure(self):
        """
        Check loaddata from fixture
        """
        presons = Person.objects.all()
        self.failUnlessEqual(presons.count(), 1)
        preson = presons[0]
        users = User.objects.all()
        self.failUnlessEqual(users.count(), 1)
        user = users[0]
        self.failUnlessEqual(user.username, 'admin')

    def test_operate(self):
        person = Person.objects.create(name='test_person_name',
                                       surname='test_person_surname',
                                       date_of_birthday=datetime.datetime.now(),
                                       email='noreply@test.com',
                                       cell_phone='1234567890',
                                       address='some address',
                                       curriculum_vita='some CV')

        self.failUnlessEqual(Person.objects.all().count(), 2)
        self.failUnlessEqual(person.name, 'test_person_name')
        person_id = person.id
        person.name = 'other_person_name'
        person.save()
        person = Person.objects.get(id=person_id)
        self.failUnlessEqual(person.name, 'other_person_name')
        person.delete()
        self.failUnlessEqual(Person.objects.all().count(), 1)

    def test_index(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 302)

