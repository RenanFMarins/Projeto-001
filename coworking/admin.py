from django.contrib import admin
from .models import Category, Coworking


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Coworking)
class CoworkingAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
