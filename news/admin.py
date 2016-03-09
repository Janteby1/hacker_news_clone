from django.contrib import admin
from .models import Post, Comment

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post)
admin.site.register(Comment)


'''
U: Janteby1
P: this is cool
'''