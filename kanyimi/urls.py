from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from core.views import frontpage, contact, about

from store.views import product_detail, category_detail, search
from userprofile.views import signup, myaccount



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('store/', include('store.urls')),
    path('userprofile/', include('userprofile.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
