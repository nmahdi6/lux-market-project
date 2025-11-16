from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order','provider','amount','status','created_at')
    search_fields = ('transaction_id','order__id')
    list_filter = ('status','provider')
