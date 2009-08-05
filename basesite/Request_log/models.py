from django.db import models
from django.contrib.auth.models import User

class Request_log(models.Model):
    request_url = models.CharField(max_length=255)
    stamp = models.DateTimeField(auto_now_add=True)
    ipaddress = models.IPAddressField()
    user = models.ForeignKey(User, null=True)
