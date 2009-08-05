from django.conf import settings

def template(request):
    return dict(SETTINGS=settings)
