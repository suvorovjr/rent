from django import template

register = template.Library()


@register.filter(name='add_placeholder')
def add_placeholder(subject_form, placeholder):
    return subject_form.as_widget(attrs={'placeholder': placeholder})


@register.filter(name='add_class')
def add_class(subject_form, castom_class):
    return subject_form.as_widget(attrs={'class': castom_class})
