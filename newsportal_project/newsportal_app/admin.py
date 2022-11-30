from django.contrib import admin
from .models import Post, Comment, PostCategory, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Category)


