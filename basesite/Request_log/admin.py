'''Here activate admin for RequestLog model'''

from django.contrib import admin
from basesite.Request_log.models import RequestLog

admin.site.register(RequestLog)
