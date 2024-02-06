from django.urls import path
from realty.views import index, RealtyCreateView
from realty.apps import RealtyConfig

app_name = RealtyConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('realty/create/', RealtyCreateView.as_view(), name='create'),
    # path('search_realty', ..., name='search_realty'),
    # path('create_realty', ..., name='create_realty'),
    # path('update_realty', ..., name='update_realty'),
    # path('delete_realty', ..., name='delete_realty'),
]