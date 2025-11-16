from django.db import models


class Attribute(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="نام ویژگی"
    )
    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی‌ها"
        ordering = ("name",)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        related_name='values',
        on_delete=models.CASCADE,
        verbose_name="ویژگی"
    )
    value = models.CharField(
        max_length=200,
        verbose_name="مقدار ویژگی"
    )

    class Meta:
        unique_together = ('attribute', 'value')
        verbose_name = "مقدار ویژگی"
        verbose_name_plural = "مقادیر ویژگی‌ها"
        ordering = ("attribute", "value")

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"
