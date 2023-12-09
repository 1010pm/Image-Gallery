# في ملف myapp/urls.py (أو أي اسم قد قمت بإعطائه لتطبيقك)
from django.urls import path
from .views import home, upload_image
from django.conf import settings
from django.conf.urls.static import static
from .views import home, upload_image, delete_image
urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_image, name='upload_image'),
    path('delete/<int:image_id>/', delete_image, name='delete_image'),
]
# إضافة الكود التالي لدعم تحميل الوسائط (الصور)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





