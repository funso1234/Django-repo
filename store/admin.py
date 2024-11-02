from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product, Collection


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description', 'inventory_status']
    list_per_page = 10
    list_editable = ['price']
    search_fields = ['title', 'description']

    @admin.display(description='inventory')
    def inventory_status(self, product:Product):
        if product.inventory < 20:
            return 'Low'
        return 'Ok'

    @admin.register(Collection)
    class CollectionAdmin(admin.ModelAdmin):
        list_display = ['id','title','product_count']
        list_per_page = 10
        search_fields = ['id','title']


        @admin.display(ordering='Collection')
        def product_count(self, collection:Collection):
            return collection.product_set.count()





# @admin.register(Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description']
#     list_per_page = 10
#     list_editable = ['description']
#     search_fields = ['name']
#     @admin.display(description='description')
#     def description(self, collection:Collection):
#         if collection.inventory < 20:
#         return collection.description
#     return 'OK'


# Register your models here.
