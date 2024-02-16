from django.contrib import admin
from .models import Category, Author, Comment, Post


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post)
