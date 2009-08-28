'''Custom tags'''

from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def admin_edit_url(incoming_object):
    '''Simple tag for templates.
    Return url for object edit page in djando admin'''

    return reverse("admin:%s_%s_change" % (incoming_object._meta.app_label,
                                           incoming_object._meta.module_name),
                   args=(incoming_object.id,))
