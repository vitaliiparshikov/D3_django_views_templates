from django import template


register = template.Library()


SYM_LIST = ['Победитель', 'Новый']


@register.filter()
def censor(value):
    for item in SYM_LIST:
        value = value.replace(item[1:], '*' * len(item[1:]))
    return value
