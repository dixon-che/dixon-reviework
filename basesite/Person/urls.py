'''urls config for Person views'''

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('basesite.Person.views',
    url(r'^(?P<person_id>\d+)/edit/$', 'edit', name='person-edit'),
)
