from django import forms
from users.forms import StylesMixin
from news.models import News


class NewsForm(StylesMixin, forms.ModelForm):
    class Meta:
        model = News
        exclude = ('views_count', 'is_active', 'slug')

        def clean_title(self):
            title = self.cleaned_data['title']
            bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                         'радар']
            for word in bad_words:
                if word in title.lower():
                    raise forms.ValidationError("Описание продукта содержит запрещенное слово.")
            return title

        def clean_description(self):
            description = self.cleaned_data['body']
            bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                         'радар']
            for word in bad_words:
                if word in description.lower():
                    raise forms.ValidationError("Описание продукта содержит запрещенное слово.")
            return description
