from django.db import models
from django.utils import timezone

class ShippingMethod(models.Model):
    name = models.CharField(max_length=200, verbose_name="روش ارسال")
    code = models.CharField(max_length=50, blank=True, verbose_name="کد")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="هزینه ارسال")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "روش ارسال"
        verbose_name_plural = "روش‌های ارسال"

    def __str__(self):
        return self.name

class Shipment(models.Model):
    order = models.ForeignKey('order.Order', related_name='shipments', on_delete=models.CASCADE, verbose_name="سفارش")
    method = models.ForeignKey(ShippingMethod, on_delete=models.SET_NULL, null=True, verbose_name="روش ارسال")
    tracking_number = models.CharField(max_length=200, blank=True, verbose_name="شماره پیگیری")
    shipped_at = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ ارسال")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "ارسال"
        verbose_name_plural = "ارسال‌ها"

    def __str__(self):
        return f"{self.order} — {self.method}"
