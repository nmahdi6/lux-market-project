from django.contrib import admin
from .models import Product, ProductVariant, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    verbose_name = "تصویر"
    verbose_name_plural = "تصاویر"


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    fields = ('sku', 'price', 'compare_at_price', 'is_active')
    verbose_name = "واریانت"
    verbose_name_plural = "واریانت‌ها"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'is_active', 'created_at')
    list_filter = ('is_active', 'brand', 'categories')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline, ProductVariantInline]

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('sku', 'product', 'price', 'is_active')
    search_fields = ('sku', 'product__title')
    filter_horizontal = ('option_values', 'attributes')

    class Meta:
        verbose_name = "واریانت محصول"
        verbose_name_plural = "واریانت‌های محصول"
