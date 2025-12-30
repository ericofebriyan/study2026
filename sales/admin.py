from django.contrib import admin
from django.utils.html import format_html
from .models import Perfume


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'name', 'brand', 'price', 'stock')
    search_fields = ('name', 'brand')
    list_filter = ('brand',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;"/>', obj.image.url)
        return '(no image)'
    image_tag.short_description = 'Gambar'
