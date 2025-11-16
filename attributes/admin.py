from django.contrib import admin
from .models import Attribute, AttributeValue


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1
    verbose_name = "مقدار ویژگی"
    verbose_name_plural = "مقادیر ویژگی"


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی‌ها"


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value')
    search_fields = ('value',)
    ordering = ('attribute', 'value')

    class Meta:
        verbose_name = "مقدار ویژگی"
        verbose_name_plural = "مقادیر ویژگی‌ها"
