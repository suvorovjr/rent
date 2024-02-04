from django import forms
from users.forms import StylesMixin
from news.models import News


class NewsForm(StylesMixin, forms.ModelForm):
    class Meta:
        model = News
        exclude = ('views_count', 'is_active', 'slug')
