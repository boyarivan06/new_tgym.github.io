from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from tgym.forms import NewBlogForm, NewPostForm, NewPhotoForm, NewPhotoAlbumForm
from tgym.models import User, Blog, Post, Photo, PhotoAlbum
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = dict()
    news = Post.objects.filter(blog_id=1).all()

    context['news'] = news
    print('start')
    return render(request, 'index.html', context)


def new_blog_page(request):
    context = dict()
    if request.method == 'POST':
        form = NewBlogForm(request.POST)
        if form.is_valid():
            title = form.data['title']
            blog = Blog(title=title, author=request.user)
            blog.save()
            return redirect(index_page)
    context['form'] = NewBlogForm()
    return render(request, 'new_blog.html', context)


def new_post_page(request):
    context = dict()
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.data['title']
            text = form.data['text']
            blog_id = form.data['blog_id']
            post = Post(title=title, text=text, blog_id=Blog.objects.filter(id=blog_id).first(), author=request.user)
            post.save()
            return redirect(index_page)
    context['form'] = NewPostForm()
    return render(request, 'new_post.html', context)


def upload_image_view(request):
    if request.method == 'POST':
        if request.POST['action_type'] == 'start':
            form = NewPhotoForm()
            album_id = request.POST['album_id']  # if request.POST['album_id'] else print('album id is none!!!')
            return render(request, 'new_photo.html', {'form': form, 'album_id': album_id})
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            album_id = int(form.data['album_id'])
            obj.photoalbum = PhotoAlbum.objects.filter(id=album_id).first()
            obj.save()
            return redirect(f'/photoalbums/{album_id}')
    else:
        form = NewPhotoForm()
    return render(request, 'new_photo.html', {'form': form})


def new_photo_album(request):
    if request.method == 'POST':
        form = NewPhotoAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            return redirect(to='index')
    else:
        form = NewPhotoAlbumForm()
    return render(request, 'new_photo_album.html', {'form': form, 'user': request.user})


def success(request):
    return HttpResponse('successfully uploaded')


def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


def photoalbums_view(request):
    data = PhotoAlbum.objects.all()
    return render(request, 'photoalbums.html', {'data': data})


def photoalbum_view(request, id):
    album = PhotoAlbum.objects.filter(id=id).first()
    if not album:
        return HttpResponseNotFound('фотоальбом не найден')
    return render(request, 'photoalbum.html', {'album': album})

def photo_view(request, id):
    photo = Photo.objects.filter(id=id).first()
    if not photo:
        return HttpResponseNotFound('фото не найдено')
    return render(request, 'photo.html', {'photo': photo})
