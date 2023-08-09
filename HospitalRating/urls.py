from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HospitalRating.common.urls')),
    path('patients/', include('HospitalRating.patients.urls')),
    path('accounts/', include('HospitalRating.accounts.urls')),
    path('doctors/', include('HospitalRating.doctors.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
