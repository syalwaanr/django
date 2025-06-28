# tugasku/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve  # <- tambahan

from artikel import views
from tugasku.authentication import login, logout, registrasi

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')), 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('artikel/<int:id>/', views.detail_artikel, name='detail_artikel'),
    path('about/', views.about_author, name='about_author'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('artikel_list', views.artikel_list, name='artikel_list'),

    # Auth
    path('auth-login', login, name='login'),
    path('auth-logout', logout, name='logout'),
    path('auth-registrasi', registrasi, name='registrasi'),

    # Artikel dashboard routes
    path('dashboard/', include("artikel.urls")),
]

# Static files (CSS, JS)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

# MEDIA FILES (gambar upload user)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Menangani media saat di production (DEBUG=False)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
