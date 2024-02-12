from django.contrib import admin

from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'model',
        'brand',
        'factory_year',
        'model_year',
        'value',
        '_has_photo',
    )
    search_fields = ('model',)
    list_filter = (
        'brand',
        'factory_year',
        'model_year',
    )

    def _has_photo(self, obj):
        if obj.photo:
            return True
        return False

    _has_photo.boolean = True


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
