from django.urls import path
from realty.views import IndexView, RealtyCreateView, RealtyListView
from realty.apps import RealtyConfig

app_name = RealtyConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('realty/create/', RealtyCreateView.as_view(), name='create'),
    path('realty/list/', RealtyListView.as_view(), name='list'),
    # path('search_realty', ..., name='search_realty'),
    # path('create_realty', ..., name='create_realty'),
    # path('update_realty', ..., name='update_realty'),
    # path('delete_realty', ..., name='delete_realty'),
]
