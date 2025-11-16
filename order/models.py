from django.db import models
from django.utils import timezone

ORDER_STATUS = (
    ('PENDING','در انتظار پرداخت'),
    ('PAID','پرداخت شده'),
    ('PROCESSING','در حال پردازش'),
    ('SHIPPED','ارسال شده'),
    ('CANCELLED','لغو شده'),
    ('COMPLETED','تکمیل شده'),
)

class Order(models.Model):
    customer = models.ForeignKey('customer.Customer', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="مشتری")
    guest_email = models.EmailField(blank=True, verbose_name="ایمیل مهمان")
    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="مبلغ کل")
    status = models.CharField(max_length=32, choices=ORDER_STATUS, default='PENDING', verbose_name="وضعیت سفارش")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین به‌روزرسانی")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"

    def __str__(self):
        return f"#{self.id} — {self.customer or self.guest_email} — {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="سفارش")
    variant = models.ForeignKey('product.ProductVariant', on_delete=models.PROTECT, verbose_name="واریانت")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="مبلغ واحد")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="مبلغ کل آیتم")

    class Meta:
        verbose_name = "آیتم سفارش"
        verbose_name_plural = "آیتم‌های سفارش"

    def __str__(self):
        return f"{self.variant} x{self.quantity}"
