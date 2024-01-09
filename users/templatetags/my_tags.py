from django import template

register = template.Library()


@register.filter(name='add_placeholder')
def add_placeholder(subject_form, placeholder):
    return subject_form.as_widget(attrs={'placeholder': placeholder})
