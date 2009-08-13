'''main urls config'''
from django.conf.urls.defaults import patterns, include
#, handler404, handler500
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'basesite.Person.views.main_page'),
    (r'^login/$',
     'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^person/', include('basesite.Person.urls')),

    (r'^admin/', include(admin.site.urls)),
)
