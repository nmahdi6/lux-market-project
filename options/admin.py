from django.contrib import admin
from .models import Option, OptionValue


class OptionValueInline(admin.TabularInline):
    model = OptionValue
    extra = 1
    verbose_name = "مقدار گزینه"
    verbose_name_plural = "مقادیر گزینه‌ها"


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    inlines = [OptionValueInline]
    list_display = ('name', 'position')
    ordering = ('position',)
    search_fields = ('name',)

    class Meta:
        verbose_name = "گزینه"
        verbose_name_plural = "گزینه‌ها"


@admin.register(OptionValue)
class OptionValueAdmin(admin.ModelAdmin):
    list_display = ('option', 'value', 'position')
    ordering = ('position',)
    search_fields = ('value',)

    class Meta:
        verbose_name = "مقدار گزینه"
        verbose_name_plural = "مقادیر گزینه‌ها"
