from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

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


class NewCarView(View):
    def get(self, request):
        new_car_form = CarForm()
        return render(
            request=request,
            template_name='new_car.html',
            context={'new_car_form': new_car_form},
        )

    def post(self, request):
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(
            request=request,
            template_name='new_car.html',
            context={'new_car_form': new_car_form},
        )
