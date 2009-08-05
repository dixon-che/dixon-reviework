from django.conf.urls.defaults import patterns, url, include, handler404, handler500
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    (r'^$', 'basesite.Person.views.main_page'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^person/', include('basesite.Person.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
