'''Here activate admin for ModelLog model'''

from django.contrib import admin
from basesite.db_log.models import ModelLog

admin.site.register(ModelLog)
