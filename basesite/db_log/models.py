'''Module with ModelLog model'''

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from basesite.Request_log.models import RequestLog
from django.contrib.auth.models import Message
from django.contrib.sessions.models import Session


EVENT_CHOICES = (
    ('create', 'create'),
    ('edit', 'edit'),
    ('delete', 'delete'),
    )


class ModelLog(models.Model):
    '''Model store info about model objects activity
    creating/editing/deleting'''

    object_log = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    event = models.CharField(max_length=6, choices=EVENT_CHOICES)
    stamp = models.DateTimeField(auto_now_add=True)


EVENT_CHOICES_DICT = {None: 'delete',
                      True: 'create',
                      False: 'edit'}


def event_callback(sender, instance, **kwargs):
    '''callback for signals  creating/editing/deleting objects
    store to model ModelLog this events'''

    if sender not in (ModelLog, RequestLog, Message, Session):#no loged modlels
        content_type = ContentType.objects.get_for_model(sender)
        ModelLog.objects.create(object_log=content_type,
                                object_id=instance.id,
                                event=EVENT_CHOICES_DICT[kwargs.get('created',
                                                                    None)])


post_save.connect(event_callback)
post_delete.connect(event_callback)
