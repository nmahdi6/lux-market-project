from django.db import models
from django.utils import timezone

class Coupon(models.Model):
    code = models.CharField(max_length=80, unique=True, verbose_name="کد تخفیف")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="درصد تخفیف")
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="مبلغ ثابت تخفیف")
    active = models.BooleanField(default=True, verbose_name="فعال")
    valid_from = models.DateTimeField(default=timezone.now, verbose_name="شروع معتبر بودن")
    valid_until = models.DateTimeField(null=True, blank=True, verbose_name="پایان معتبر بودن")
    usage_limit = models.PositiveIntegerField(null=True, blank=True, verbose_name="حد اکثر استفاده")

    class Meta:
        verbose_name = "کوپن"
        verbose_name_plural = "کوپن‌ها"

    def __str__(self):
        return self.code

class CouponUsage(models.Model):
    coupon = models.ForeignKey(Coupon, related_name='usages', on_delete=models.CASCADE, verbose_name="کوپن")
    order = models.ForeignKey('order.Order', related_name='coupon_usages', on_delete=models.CASCADE, verbose_name="سفارش")
    used_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ استفاده")

    class Meta:
        verbose_name = "استفاده از کوپن"
        verbose_name_plural = "استفاده‌های کوپن"
