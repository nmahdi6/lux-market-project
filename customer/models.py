from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="کاربر (اختیاری)")
    full_name = models.CharField(max_length=250, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=50, blank=True, verbose_name="تلفن")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"
        ordering = ("full_name",)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Address(models.Model):
    customer = models.ForeignKey(Customer, related_name='addresses', on_delete=models.CASCADE, verbose_name="مشتری")
    title = models.CharField(max_length=120, blank=True, verbose_name="عنوان آدرس (مثلاً خانه/محل کار)")
    full_name = models.CharField(max_length=250, verbose_name="نام گیرنده")
    phone = models.CharField(max_length=50, verbose_name="تلفن گیرنده")
    province = models.CharField(max_length=200, verbose_name="استان")
    city = models.CharField(max_length=200, verbose_name="شهر")
    address = models.TextField(verbose_name="آدرس کامل")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name="کد پستی")
    is_default = models.BooleanField(default=False, verbose_name="آدرس پیش‌فرض")

    class Meta:
        verbose_name = "نشانی"
        verbose_name_plural = "نشانی‌ها"

    def __str__(self):
        return f"{self.title or self.full_name} — {self.city}"
