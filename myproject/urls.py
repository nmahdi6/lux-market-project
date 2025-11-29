from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _ 


admin.site.site_header = _("مدیریت ")
admin.site.site_title = _("وبگاه")
admin.site.index_title = _("خوش آمدید")

urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحات عمومی
    path('', include('core.urls', namespace='core')),

    # صفحات احراز هویت
    path('', include('customer.urls', namespace='customer')),

    # پنل کاربر
    path("account/", include(("account.urls"), namespace='account')),

    # پنل فروشنده
    path("seller/", include(("seller.urls"), namespace='seller')),

    # محصول
    path('product/', include('product.urls', namespace='product')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)