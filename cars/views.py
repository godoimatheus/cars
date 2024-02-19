from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarForm
from cars.models import Car


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('-id')
        search = request.GET.get('search')
        if search:
            cars = Car.objects.filter(model__icontains=search)

        return render(
            request=request,
            template_name='cars.html',
            context={'cars': cars},
        )


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
