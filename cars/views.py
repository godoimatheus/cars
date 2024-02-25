from django.views.generic import CreateView, ListView

from cars.forms import CarForm
from cars.models import Car


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset


class NewCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'
