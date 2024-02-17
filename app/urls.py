from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import register_view
from cars.views import cars_view, new_car_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view, name='cars_list'),
    path('new-car/', new_car_view, name='new_car'),
    path('register/', register_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
