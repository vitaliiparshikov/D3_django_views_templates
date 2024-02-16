from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-date_create'
    template_name = 'list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
