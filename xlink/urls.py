from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from xlink import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('accounts/', views.index, name="index"),
    path("", views.home, name="home"),
    path('accounts-auth/', include('allauth.urls')),
    # path('profile-create/',views. )
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)