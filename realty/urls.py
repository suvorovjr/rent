from django.urls import path
from realty.views import IndexView, RealtyCreateView, RealtyListView, RealtyDetailView, RealtyUpdateView, \
    RealtyDeleteView
from django.views.decorators.cache import cache_page
from realty.apps import RealtyConfig

app_name = RealtyConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('realty/create/', RealtyCreateView.as_view(), name='create'),
    path('realty/list/', RealtyListView.as_view(), name='list'),
    path('realty/view/<int:pk>/', cache_page(60)(RealtyDetailView.as_view()), name='view'),
    path('realty/delete/<int:pk>/', RealtyDeleteView.as_view(), name='delete'),
    path('realty/update/<int:pk>/', RealtyUpdateView.as_view(), name='update'),
]
