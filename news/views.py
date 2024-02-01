from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from news.forms import NewsForm
from news.models import News


class NewsCreationView(CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('rent:index')


class NewsDetailView(DetailView):
    model = News


class NewsUpdateView(UpdateView):
    model = News


class NewsDeleteView(DeleteView):
    model = News
