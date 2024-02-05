from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from realty.models import Realty


def index(request):
    return render(request, 'realty/index.html')


# class RealtyUpdateCreateMixin:
#     model = Realty
#     fields = ('room', '_type', 'transaction', 'description', 'price', 'floor', 'max_floor', 'square')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['foto_form'] = PhotoForm()
#         return context
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         files = self.request.FILES.getlist('files')
#         with transaction.atomic():
#             self.object = form.save()
#             if files:
#                 img_lst = [RealtyPhoto(house=self.object, foto=file) for file in files]
#                 RealtyPhoto.objects.bulk_create(img_lst)
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         return reverse('realty:index')


class RealtyCreateView(CreateView):
    model = Realty
    fields = ('room', '_type', 'transaction', 'description', 'price', 'floor', 'max_floor', 'square')
    success_url = reverse_lazy('realty:index')
