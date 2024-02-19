import django_filters
from realty.models import Realty, Rooms, TypeRealty, TypeTransaction


class RealtyFilter(django_filters.FilterSet):
    realty_type = django_filters.ModelChoiceFilter(field_name='realty_type', queryset=TypeRealty.objects.all())
    transaction_type = django_filters.ModelChoiceFilter(field_name='transaction', queryset=TypeTransaction.objects.all())
    rooms = django_filters.ModelChoiceFilter(field_name='room', queryset=Rooms.objects.all())

    class Meta:
        model = Realty
        fields = ('realty_type', 'transaction', 'room')
