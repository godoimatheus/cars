from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
from cars.views import CarsView, new_car_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsView.as_view(), name='cars_list'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('new-car/', new_car_view, name='new_car'),
    path('register/', register_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
