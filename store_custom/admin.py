from django.contrib import admin
from store.admin import ProductAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem
from store.models import Product

class TagInline(GenericTabularInline):
    autocomplete_fields=['tag']
    extra = 0
    model = TaggedItem

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
