from django.http import HttpResponse
from django.shortcuts import render, redirect
from tgym.forms import NewBlogForm, NewPostForm, NewPhotoForm, NewPhotoAlbumForm
from tgym.models import User, Blog, Post
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
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
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
