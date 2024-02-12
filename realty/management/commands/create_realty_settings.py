from django.core.management import BaseCommand
from realty.models import TypeRealty, TypeTransaction, Rooms


class Command(BaseCommand):
    def handle(self, *args, **options):
        realty_type_list = ['Квартира', 'Дом', 'Студия', 'Коммерческая недвижимость', 'Комната']
        for realty_type in realty_type_list:
            new_realty_type = TypeRealty.objects.create(name=realty_type)
            new_realty_type.save()
        transaction_type_list = ['Продажа', 'Долгосрочная аренда', 'Посуточная аренда']
        for transaction_type in transaction_type_list:
            new_transaction_type = TypeTransaction.objects.create(transaction=transaction_type)
            new_transaction_type.save()
        room_list = [1, 2, 3, 4, 5, 6]
        for room in room_list:
            new_room = Rooms.objects.create(number=room)
            new_room.save()
