"""dj_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tgym import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('new_blog/', views.new_blog_page, name='new_blog'),
    path('new_post/', views.new_post_page, name='new_post'),
    # path('accounts/', include('registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('image_upload/', views.upload_image_view, name='image_upload'),
    path('success/', views.success, name='success'),
    path('new_photo_album/', views.new_photo_album, name='new_photo_album'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('photoalbums/', views.photoalbums_view, name='photoalbums'),
    path('photoalbums/<int:id>', views.photoalbum_view),
    path('photo/<int:id>', views.photo_view)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
