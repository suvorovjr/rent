from django.urls import path
from news.apps import NewsConfig
from news.views import NewsCreationView, NewsListView, NewsDetailView, NewsUpdateView

app_name = NewsConfig.name

urlpatterns = [
    path('create/', NewsCreationView.as_view(), name='create'),
    path('list/', NewsListView.as_view(), name='list'),
    path('view/<str:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('update/<str:slug>/', NewsUpdateView.as_view(), name='update'),

    # path('search_realty', ..., name='search_realty'),
    # path('create_news', ..., name='create_news'),
    # path('update_realty', ..., name='update_realty'),
    # path('delete_realty', ..., name='delete_realty'),
]
