from django.contrib import admin
from store.models import Product, Category ,Customer, Order



class AdminProduct(admin.ModelAdmin):
    list_display=['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Customer)
admin.site.register(Order)
