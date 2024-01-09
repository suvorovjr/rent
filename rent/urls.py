from django.urls import path
from rent.views import index, rooms
from rent.apps import RentConfig

app_name = RentConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('rooms', rooms, name='rooms'),
    # path('search_realty', ..., name='search_realty'),
    # path('create_realty', ..., name='create_realty'),
    # path('update_realty', ..., name='update_realty'),
    # path('delete_realty', ..., name='delete_realty'),
]