from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
from cars.views import CarsListView, NewCarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('new-car/', NewCarView.as_view(), name='new_car'),
    path('register/', register_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
