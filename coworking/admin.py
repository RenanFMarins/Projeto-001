from django.contrib import admin
from .models import Category, Coworking, Country, State, Municipality, Neighborhood


class CategoryAdmin(admin.ModelAdmin):
    ...


class CountryAdmin(admin.ModelAdmin):
    ...


class StateAdmin(admin.ModelAdmin):
    ...


class MunicipalityAdmin(admin.ModelAdmin):
    ...


class NeighborhoodAdmin(admin.ModelAdmin):
    ...


@admin.register(Coworking)
class CoworkingAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
