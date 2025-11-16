from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="نام برند"
    )
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
        verbose_name="اسلاگ"
    )
    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )
    logo = models.ImageField(
        upload_to='brands/',
        blank=True,
        null=True,
        verbose_name="لوگو"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    class Meta:
        ordering = ('name',)
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
