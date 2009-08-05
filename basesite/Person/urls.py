from django.conf.urls.defaults import patterns, url, include


urlpatterns = patterns('basesite.Person.views',
    url(r'^(?P<person_id>\d+)/edit/$', 'edit', name='person-edit'),
)
