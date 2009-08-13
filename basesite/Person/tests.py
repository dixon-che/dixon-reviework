'''Tests for Person module'''

from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User
#from django.template import RequestContext

from basesite.Person.models import Person


class PersonTest(TestCase):
    '''test manipulations with Person model and views '''

    def setUp(self):
        """
        On the way check loaddata from fixture
        """
        presons = Person.objects.all()
        self.failUnlessEqual(presons.count(), 1)
        self.preson = presons[0]
        users = User.objects.all()
        self.failUnlessEqual(users.count(), 1)
        self.user = users[0]
        self.failUnlessEqual(self.user.username, 'admin')

    def testCED(self):
        '''create/edit/delete tests'''
        person = Person.objects.create(name='test_person_name',
                                       surname='test_person_surname',
                                       date_of_birthday=datetime.now(),
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

    def testLoadIndex(self):
        '''Test main view'''
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 302)
        response = self.client.get('/', follow=True)
        self.failUnlessEqual(response.redirect_chain[0][0],
                             'http://testserver/login/?next=/')
        self.failIfEqual(response.content.find('Test work'), -1)

        self.failUnlessEqual(self.client.login(username='admin',
                                               password='111'), True)

        response = self.client.get('/')

        self.failUnlessEqual(response.status_code, 200)

    def testEditPage(self):
        '''Test Person edit page'''

        #print ''
        response = self.client.get('/')
        #print dir(response)
        #print response.content
        #print RequestContext()
        #print dir(self)
