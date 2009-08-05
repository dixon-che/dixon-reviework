from django.shortcuts import render_to_response #redirect,  get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from basesite.Person.models import Person


@login_required
def main_page(request):
    persons = Person.objects.all().order_by('name')
    return render_to_response("base.html",
                              RequestContext(request, dict(persons=persons)))
