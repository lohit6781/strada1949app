from django.contrib import admin
from .models import Collection, Product, Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_id', 'product_sku']
    search_fields = ('name', 'product_id')

class orderAdmin(admin.ModelAdmin):
    ordering = ('completed',)
    list_display = ['order_id', 'completed', 'order']
    search_fields = ('order_id',)
    readonly_fields = ['first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zip_code', 'country', 'email', 'phone', 'order', 'order_id']


admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, orderAdmin)