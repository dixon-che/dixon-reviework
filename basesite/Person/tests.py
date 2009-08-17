'''Tests for Person module'''

from django.test import TestCase
from django.contrib.auth.models import User
#from django.template import RequestContext

from basesite.Person.models import Person
from basesite.Request_log.models import RequestLog


person_test_values_dict = dict(name='test_person_name',
                               surname='test_person_surname',
                               date_of_birthday='2009-08-17',
                               email='noreply@test.com',
                               cell_phone='1234567890',
                               address='some address',
                               curriculum_vita='some CV')

person_base_values_dict = dict(curriculum_vita='http://dixon-che.getcv.com',
                               address='Kharkiv area, Slatino, Schorsa street #7',
                               cell_phone='+380(97)9279920',
                               email='dixon.che@gmail.com',
                               date_of_birthday='1982-06-25',
                               surname='Radchenko',
                               name='Aleksey')

edit_form_fields_ids = ('id_curriculum_vita', 'id_address', 'id_cell_phone',
                        'id_email', 'id_date_of_birthday',
                        'id_surname', 'id_name')


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
        person = Person()
        for field_key in person_test_values_dict.keys():
            setattr(person, field_key, person_test_values_dict[field_key])
        person.save()

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

        # check requests-log
        request_logs_count = RequestLog.objects.all().count()
        self.failUnlessEqual(request_logs_count, 4)

        # check work template context
        self.failIfEqual(response.content.find('en-us'), -1)
        self.failIfEqual(response.content.find('Ukraine/Kiev'), -1)

        # check work admin_edit_url template tag
        self.failIfEqual(response.content.find('/admin/Person/person/1/'), -1)

    def testEditPage(self):
        '''Test Person edit page'''

        self.client.login(username='admin', password='111')

        #check showing form
        response = self.client.get('/person/1/edit/')

        for field_id in edit_form_fields_ids:
            self.failIfEqual(response.content.find(field_id), -1)

        for phrase in person_base_values_dict.values():
            self.failIfEqual(response.content.find(phrase), -1)

        #check saving data from form
        response = self.client.post('/person/1/edit/', person_test_values_dict)

        for phrase in person_test_values_dict.values():
            self.failIfEqual(response.content.find(phrase), -1)

        #check email validation
        person_wrong_values_dict = person_base_values_dict
        person_wrong_values_dict['email'] = 'not email string'

        response = self.client.post('/person/1/edit/',
                                    person_wrong_values_dict)

        error_phrase = '<ul class="errorlist"><li>Enter a valid e-mail address.</li></ul>'
        self.failIfEqual(response.content.find(error_phrase), -1)
