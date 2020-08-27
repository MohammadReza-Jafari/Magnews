from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def increment(context, value, arg, **kwargs):
    value += int(arg)
    context[kwargs['variable_name']] = value
    return ''
