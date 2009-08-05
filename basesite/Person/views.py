from django.shortcuts import render_to_response #redirect,  get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.forms import ModelForm


from basesite.Person.models import Person


@login_required
def main_page(request):
    persons = Person.objects.all().order_by('name')
    return render_to_response("base.html",
                              RequestContext(request, dict(persons=persons)))


class PersonEditForm(ModelForm):
    class Meta:
        model = Person


@login_required
def edit(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonEditForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
    else:
        form = PersonEditForm(instance=person)
    return render_to_response("person_edit.html",
                              RequestContext(request, dict(form=form, person=person)))
