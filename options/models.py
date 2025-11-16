from django.db import models

class Option(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="نام گزینه"   # مثال: سایز، رنگ
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="اولویت نمایش"
    )

    class Meta:
        verbose_name = "گزینه"
        verbose_name_plural = "گزینه‌ها"
        ordering = ('position',)

    def __str__(self):
        return self.name


class OptionValue(models.Model):
    option = models.ForeignKey(
        Option,
        related_name='values',
        on_delete=models.CASCADE,
        verbose_name="گزینه"
    )
    value = models.CharField(
        max_length=150,
        verbose_name="مقدار"        # مثال: L ، M ، قرمز
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="اولویت نمایش"
    )

    class Meta:
        verbose_name = "مقدار گزینه"
        verbose_name_plural = "مقادیر گزینه‌ها"
        unique_together = ('option', 'value')
        ordering = ('position',)

    def __str__(self):
        return f"{self.option.name}: {self.value}"
