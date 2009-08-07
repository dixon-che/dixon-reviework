from django import template

register = template.Library()

@register.simple_tag
def admin_edit_url(incoming_object):
    return '/admin/%s/%s/%s/' % (incoming_object._meta.app_label,
                                 incoming_object._meta.module_name,
                                 incoming_object.id)
