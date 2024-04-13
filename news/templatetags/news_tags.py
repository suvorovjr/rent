from django import template

register = template.Library()


@register.filter()
def get_views(views_count):
    if views_count % 10 == 1 and views_count != 11:
        return 'просмотр'
    elif views_count % 10 in [2, 3, 4] and views_count not in [11, 12, 13, 14]:
        return 'просмотра'
    else:
        return 'просмотров'


@register.filter(name='get_number_rooms')
def get_number_rooms(rooms):
    int_room = int(rooms)
    if int_room % 10 == 1 and int_room != 11:
        return 'Комната'
    elif int_room % 10 in [2, 3, 4] and int_room not in [11, 12, 13, 14]:
        return 'Комнаты'
    else:
        return 'Комнат'

