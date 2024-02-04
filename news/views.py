from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from news.forms import NewsForm
from news.models import News
from pytils.translit import slugify


class NewsCreationView(CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('rent:index')

    def form_valid(self, form):
        if form.is_valid():
            news = form.save()
            news.slug = slugify(news.title)
            news.save()
        return super().form_valid(form)


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News


class NewsUpdateView(UpdateView):
    model = News


class NewsDeleteView(DeleteView):
    model = News
