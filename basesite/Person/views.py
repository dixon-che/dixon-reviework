'''Views for module Person'''

from django.shortcuts import render_to_response #redirect,  get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.forms import ModelForm, DateField, CharField
from django.forms.widgets import TextInput
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings

from basesite.Person.models import Person


@login_required
def main_page(request):
    '''view for index page,
    show table with info about persons  '''

    persons = Person.objects.all().order_by('name')

    return render_to_response("base.html",
                              RequestContext(request, dict(persons=persons)))


class TextInputWithMedia(TextInput):
    '''custom widget
    only add additional media link in head'''

    class Media:
        '''Adding link to js files for working AdminDateWidget'''
        js = ("/admin/jsi18n/", settings.ADMIN_MEDIA_PREFIX + "js/core.js")


class PersonEditForm(ModelForm):
    '''Model form for editing Person info'''

    name = CharField(widget=TextInputWithMedia)
    date_of_birthday = DateField(widget=AdminDateWidget())

    class Meta:
        '''Use Person model and order fields'''
        model = Person
        fields = [f.name for f in Person._meta.fields[1:].__reversed__()]

    class Media:
        '''Adding media links'''
        # I used this hack with TextInputWithMedia,
        #cose I need core.js and jsi18n before AdminDateWidget-media
        # js = ("/admin/jsi18n/", settings.ADMIN_MEDIA_PREFIX + "js/core.js")
        css = {
            'all': (settings.ADMIN_MEDIA_PREFIX + 'css/base.css', ),
            }


@login_required
def edit(request, person_id):
    '''View show form for editing Person info '''

    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonEditForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
    else:
        form = PersonEditForm(instance=person)

    return render_to_response("person_edit.html",
                              RequestContext(request, dict(form=form,
                                                           person=person)))
