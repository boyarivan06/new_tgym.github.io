from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from tgym.forms import NewBlogForm, NewPostForm, NewPhotoForm, NewPhotoAlbumForm, NewVideoForm, NewSkedForm
from tgym.models import User, Blog, Post, Photo, PhotoAlbum, Video, Sked
from django.contrib.auth.decorators import login_required
from datetime import date


def index_page(request):
    context = dict()
    news = Blog.get_by_id(1).post_set.all()

    context['news'] = news
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
            post = Post(title=title, text=text, blog_id=Blog.get_by_id(blog_id), author=request.user)
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
            obj.photoalbum = PhotoAlbum.get_by_id(album_id)
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
    data = PhotoAlbum.get_all()
    return render(request, 'photoalbums.html', {'data': data})


def photoalbum_view(request, id):
    album = PhotoAlbum.get_by_id(id)
    if not album:
        return HttpResponseNotFound('фотоальбом не найден')
    return render(request, 'photoalbum.html', {'album': album})


def photo_view(request, id):
    photo = Photo.get_by_id(id)
    if not photo:
        return HttpResponseNotFound('фото не найдено')
    return render(request, 'photo.html', {'photo': photo})


def new_video_view(request):
    if request.method == "POST":
        form = NewVideoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            return redirect(to='video')
    else:
        return render(request, 'new_video.html', {'form': NewVideoForm()})


def skeds_view(request):
    try:
        sked = Sked.objects.get_or(date=date.today())
    except Exception:
        sked = '0'
    return render(request, 'skeds.html', {'sked': sked})


'''
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
'''


@login_required
def new_sked(request):
    if request.method == "POST":
        form = NewSkedForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.save()
            return redirect(to='skeds')
        else:
            return render(request, 'new_sked.html', {'form': form})
    else:
        form = NewSkedForm()
    return render(request, 'new_sked.html', {'form': form})


def video_view(request):
    data = Video.get_all()
    return render(request, 'video.html', {'data': data})


def blogs_view(request):
    data = Blog.get_all()
    return render(request, 'blogs.html', {'data': data})


def blog_view(request, id):
    blog = Blog.get_by_id(id)
    return render(request, 'blog.html', {'blog': blog})


def post_view(request, id):
    post = Post.get_by_id(id)
    return render(request, 'post.html', {'post': post})
