from django.db import models


class Supplier(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام تأمین‌کننده"
    )
    email = models.EmailField(
        blank=True,
        verbose_name="ایمیل"
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="شماره تماس"
    )
    address = models.TextField(
        blank=True,
        verbose_name="آدرس"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )

    class Meta:
        verbose_name = "تأمین‌کننده"
        verbose_name_plural = "تأمین‌کنندگان"
        ordering = ("name",)

    def __str__(self):
        return self.name
