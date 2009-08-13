'''Custom context'''

from django.conf import settings


def template(request):
    '''return to context settings'''
    return dict(SETTINGS=settings)
