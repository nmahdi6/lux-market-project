from django.contrib import admin
from .models import Customer, Address

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0
    verbose_name = "نشانی"
    verbose_name_plural = "نشانی‌ها"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name','email','phone')
    inlines = [AddressInline]
    list_filter = ('created_at',)
    ordering = ('full_name',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer','title','city','is_default')
    search_fields = ('customer__full_name','city','postal_code')
    list_filter = ('is_default',)
