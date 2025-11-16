from django.db import models
from django.utils import timezone

RATING_CHOICES = [(i, str(i)) for i in range(1,6)]

class ProductReview(models.Model):
    product = models.ForeignKey('product.Product', related_name='reviews', on_delete=models.CASCADE, verbose_name="محصول")
    customer = models.ForeignKey('customer.Customer', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="مشتری")
    title = models.CharField(max_length=200, blank=True, verbose_name="عنوان")
    body = models.TextField(verbose_name="متن نظر")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="امتیاز")
    is_approved = models.BooleanField(default=False, verbose_name="تایید شده")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "نظر محصول"
        verbose_name_plural = "نظرات محصولات"
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.product} — {self.rating}"
