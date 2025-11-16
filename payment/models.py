from django.db import models
from django.utils import timezone

PAY_STATUS = (
    ('INIT','آغاز'),
    ('SUCCESS','موفق'),
    ('FAILED','ناموفق'),
)

class Payment(models.Model):
    order = models.ForeignKey('order.Order', related_name='payments', on_delete=models.CASCADE, verbose_name="سفارش")
    provider = models.CharField(max_length=100, verbose_name="درگاه/پرداخت‌کننده")
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="مبلغ")
    status = models.CharField(max_length=32, choices=PAY_STATUS, default='INIT', verbose_name="وضعیت پرداخت")
    transaction_id = models.CharField(max_length=200, blank=True, verbose_name="شناسه تراکنش")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انجام")

    class Meta:
        verbose_name = "پرداخت"
        verbose_name_plural = "پرداخت‌ها"

    def __str__(self):
        return f"{self.order} — {self.amount} — {self.status}"
