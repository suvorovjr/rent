from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from realty.models import Realty, RealtyPhoto
from realty.filters import RealtyFilter
from django.core.cache import cache
from django.conf import settings
from django.http import Http404
from realty.forms import RealtyForm


class IndexView(TemplateView):
    template_name = 'realty/index.html'


class RealtyCreateView(CreateView):
    model = Realty
    form_class = RealtyForm
    success_url = reverse_lazy('realty:index')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        photos = form.cleaned_data["imagine_field"]
        new_realty = form.save()
        new_realty.title = f'{new_realty.room}-к {new_realty.realty_type}, {new_realty.square}м\u00B2, {new_realty.floor}/{new_realty.max_floor} эт.'
        new_realty.owner = self.request.user
        new_realty.save()
        for photo in photos:
            realty_photo = RealtyPhoto(
                realty=new_realty,
                photo=photo
            )
            realty_photo.save()
        return super().form_valid(form)


class RealtyListView(ListView):
    model = Realty
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('photo')
        cache_key = f'news_filter_{self.request.GET.urlencode()}'
        if settings.CACHE_ENABLED:
            self.filterset = cache.get(cache_key)
            if self.filterset is None:
                self.filterset = RealtyFilter(self.request.GET, queryset=queryset)
                cache.set(cache_key, self.filterset)
        else:
            self.filterset = RealtyFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['filter'] = self.filterset
        return context_data


class RealtyDetailView(DetailView):
    model = Realty

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('photo')
        return queryset


class RealtyUpdateView(UpdateView):
    model = Realty
    form_class = RealtyForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        photos = form.cleaned_data["imagine_field"]
        new_realty = form.save()
        new_realty.title = f'{new_realty.room}-к {new_realty.realty_type}, {new_realty.square}м\u00B2, {new_realty.floor}/{new_realty.max_floor} эт.'
        new_realty.owner = self.request.user
        new_realty.save()
        for photo in photos:
            realty_photo = RealtyPhoto(
                realty=new_realty,
                photo=photo
            )
            realty_photo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:profile')


class RealtyDeleteView(DeleteView):
    model = Realty

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object
