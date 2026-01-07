from django.contrib import admin
from .models import Food, Category, Table, Order, OrderItem

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'image')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('price',) 
    ordering = ('category', 'name')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'available')

class OrderItemInline(admin.StackedInline):
    model = OrderItem
     
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'total_price', 'status', 'payment_status')
    list_editable = ('payment_status', 'status',)
    list_filter = ('status', 'payment_status',)
    search_fields = ('user__username',)
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'food',)
