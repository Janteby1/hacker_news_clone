from django.contrib import admin
from .models import Post, Comment

class AuthorAdmin(admin.ModelAdmin):
    pass

# add the models you want in your admin backend
admin.site.register(Post)
admin.site.register(Comment)

