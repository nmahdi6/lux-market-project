from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from brand.models import Brand
from category.models import Category


class Product(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="عنوان محصول"
    )
    slug = models.SlugField(
        max_length=320,
        unique=True,
        blank=True,
        verbose_name="نامک"
    )
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products',
        verbose_name="برند"
    )
    categories = models.ManyToManyField(
        Category,
        related_name='products',
        blank=True,
        verbose_name="دسته‌بندی‌ها"
    )
    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
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
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="محصول"
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name="تصویر محصول"
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن جایگزین"
    )
    ordering = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش"
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصول"

    def __str__(self):
        return f"تصویر {self.product.title}"


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='variants',
        on_delete=models.CASCADE,
        verbose_name="محصول"
    )
    sku = models.CharField(
        max_length=128,
        unique=True,
        verbose_name="کد SKU"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="قیمت"
    )
    compare_at_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="قیمت قبل"
    )
    option_values = models.ManyToManyField(
        'options.OptionValue',
        blank=True,
        related_name='variants',
        verbose_name="گزینه‌ها"
    )
    attributes = models.ManyToManyField(
        'attributes.AttributeValue',
        blank=True,
        related_name='variants',
        verbose_name="ویژگی‌ها"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )
    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="وزن (کیلوگرم)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    class Meta:
        verbose_name = "واریانت محصول"
        verbose_name_plural = "واریانت‌های محصول"

    def __str__(self):
        return f"{self.product.title} — {self.sku}"
