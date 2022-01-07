from django import template

register = template.Library()


@register.filter(name='add_class')
def disable(value, arg):
    pass
