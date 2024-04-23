from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from xlink import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileEditView
urlpatterns = [
    path('accounts/', views.index, name="index"),
    path("", views.accounts, name="home"),
    path('accounts-auth/', include('allauth.urls')),
    path('profile-create/',views.form_create, name="account" ),
    path("class/create.html", views.form_class, name="createclass"),
    path('account/<str:name>/', views.room, name="room"),
    path('community/<str:name>/', views.community, name="community"),
    path('community/comment/<str:name>/', views.form_comment, name="comment"),
    path('compose/recomments/<int:pk>/<str:name>/', views.form_return, name="form_return"),
    path('follow_count', views.follow_count, name="follow_count"),
    path('root_selecter', views.root_selecter, name="root_select"),
    path('follow_count', views.follow_count, name="follow_counts"),
    path('root_count', views.root_count, name="root_count"),
    # path("account/<slug:slug>/edit/", views.form_edit , name="profile_edit"),
    # path("community/<slug:slug>/edit/", views.form_class_edit, name="form_class_edit"),
    re_path(r'community/(?P<slug>[\w\.]+)/edit/', views.form_class_edit, name='form_class_edit'),
    re_path(r'account/(?P<slug>[\w\.]+)/edit/', views.form_edit, name='profile_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)