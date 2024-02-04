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
