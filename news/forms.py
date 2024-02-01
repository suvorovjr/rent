from django import forms
from users.forms import StylesMixin
from news.models import News


class NewsForm(StylesMixin, forms.ModelForm):
    class Meta:
        model = News
        fields = ('__all__')
        exclude = ('views_count', 'is_active', 'slug')
