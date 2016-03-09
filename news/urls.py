from django.conf.urls import include, url
from django.contrib import admin
from news import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^register$', views.User_Register.as_view(), name='register'),
    url(r'^login$', views.User_Login.as_view(), name='login'),
    url(r'^logout$', views.User_Logout.as_view(), name='logout'),

    url(r'^create$', views.Create_Post.as_view(), name="create"),
    # here we send the url to the views witht he slug id attached to it
    url(r'^delete/(?P<post_slug>[A-Za-z0-9\-\_]+)$', views.Delete_Post.as_view(), name='delete'),
    url(r'^edit/(?P<post_slug>[A-Za-z0-9\-\_]+)$', views.Edit_Post.as_view(), name="edit"),

    url(r'^comment/(?P<post_slug>[A-Za-z0-9\-\_]+)$', views.Add_Comment.as_view(), name='comment'),
    url(r'^edit_comment/(?P<comment_slug>[A-Za-z0-9\-\_]+)$', views.Edit_Comment.as_view(), name='edit_comment'),
    url(r'^delete_comment/(?P<comment_slug>[A-Za-z0-9\-\_]+)$', views.Delete_Comment.as_view(), name='delete_comment'),
]

