from django.db import models
from django.utils import timezone
from product.models import ProductVariant


class Warehouse(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام انبار"
    )
    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="کد انبار"
    )
    address = models.TextField(
        blank=True,
        verbose_name="آدرس"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"

    def __str__(self):
        return self.name


class Stock(models.Model):
    variant = models.ForeignKey(
        ProductVariant,
        related_name='stocks',
        on_delete=models.CASCADE,
        verbose_name="واریانت محصول"
    )
    warehouse = models.ForeignKey(
        Warehouse,
        related_name='stocks',
        on_delete=models.CASCADE,
        verbose_name="انبار"
    )
    quantity = models.IntegerField(
        default=0,
        verbose_name="موجودی"
    )

    class Meta:
        unique_together = ('variant', 'warehouse')
        verbose_name = "موجودی"
        verbose_name_plural = "موجودی‌ها"

    def __str__(self):
        return f"{self.variant.sku} @ {self.warehouse.name}: {self.quantity}"


class StockOperation(models.Model):
    OP_TYPES = (
        ('IN', 'ورود'),
        ('OUT', 'خروج'),
        ('ADJ', 'تعدیل'),
    )

    variant = models.ForeignKey(
        ProductVariant,
        related_name='operations',
        on_delete=models.CASCADE,
        verbose_name="واریانت محصول"
    )
    warehouse = models.ForeignKey(
        Warehouse,
        related_name='operations',
        on_delete=models.CASCADE,
        verbose_name="انبار"
    )
    op_type = models.CharField(
        max_length=3,
        choices=OP_TYPES,
        verbose_name="نوع عملیات"
    )
    quantity = models.IntegerField(
        verbose_name="مقدار"
    )
    note = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ ثبت"
    )

    class Meta:
        verbose_name = "عملیات موجودی"
        verbose_name_plural = "عملیات موجودی‌ها"

    def __str__(self):
        return f"{self.variant.sku} - {self.op_type} - {self.quantity}"
