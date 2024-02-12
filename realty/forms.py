from django import forms
from realty.models import Realty
from users.forms import StylesMixin


class MultipleImagineInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImagineField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImagineInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class RealtyForm(StylesMixin, forms.ModelForm):
    imagine_field = MultipleImagineField()

    class Meta:
        model = Realty
        exclude = ('title', 'owner')
