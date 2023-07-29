from django.contrib import admin
from tgym.models import Post, Blog, Photo, PhotoAlbum

# Register your models here.
admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Photo)
admin.site.register(PhotoAlbum)
