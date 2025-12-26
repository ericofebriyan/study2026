from django.contrib import admin
from .models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'stock')
    search_fields = ('name', 'brand')
    list_filter = ('brand',)
