from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductPhotoInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Raiting)
admin.site.register(Reveiw)
admin.site.register(Category)

