import django_filters
from news.models import News, Categories


class CharBaseFilter(django_filters.ModelChoiceFilter, django_filters.CharFilter):
    pass


class NewsFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(field_name='category', queryset=Categories.objects.all())

    class Meta:
        model = News
        fields = ('category',)
