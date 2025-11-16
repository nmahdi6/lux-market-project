from django.contrib import admin
from .models import ProductReview

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product','customer','rating','is_approved','created_at')
    list_filter = ('is_approved','rating')
    search_fields = ('product__title','customer__full_name','body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} نظر تایید شد.")
    approve_reviews.short_description = "تأیید انتخاب‌شده‌ها"
