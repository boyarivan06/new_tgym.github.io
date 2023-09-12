from django.forms import HiddenInput, Form, ModelForm, IntegerField, CharField, PasswordInput
from tgym.models import Photo, PhotoAlbum, Video, Blog, Post, Sked


class NewBlogForm(Form):
    title = CharField(label='Заголовок блога', required=True)


class NewPostForm(Form):
    title = CharField(label='Заголовок поста', required=True)
    text = CharField(label='Текст поста')
    blog_id = IntegerField(label='blog_id')


class NewPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['label', 'image']


class NewPhotoAlbumForm(ModelForm):
    class Meta:
        model = PhotoAlbum
        fields = ['title', 'comment', 'image']


class NewVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['video_source', 'label']


class NewSkedForm(ModelForm):
    class Meta:
        model = Sked
        fields = ['date', 'file']
