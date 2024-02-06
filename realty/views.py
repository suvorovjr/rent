from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from realty.models import Realty, RealtyPhoto
from realty.forms import RealtyForm


def index(request):
    return render(request, 'realty/index.html')


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

    # Replace with your URL or reverse().
