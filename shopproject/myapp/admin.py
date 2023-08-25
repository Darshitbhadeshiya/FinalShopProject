from django.contrib import admin
from .models import product,ImageModel
from django.utils.html import format_html
# Register your models here.

# admin.site.register(product)


# Register your models here.
class AllData(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['title','image_tag',]

admin.site.register(product,AllData)