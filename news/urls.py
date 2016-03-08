from django.conf.urls import include, url
from django.contrib import admin
from news import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^register$', views.User_Register.as_view(), name='register'),
    url(r'^login$', views.User_Login.as_view(), name='login'),
    url(r'^logout$', views.User_Logout.as_view(), name='logout'),

    # url(r'^create$', views.Create_Post.as_view(), name="create"),
    # url(r'^edit/(?P<post_slug>[A-Za-z0-9\-\_]+)$', Edit_Post.as_view(), name="edit"),
    # url(r'^delete/(?P<post_slug>[A-Za-z0-9\-\_]+)$', Delete_Post.as_view(), name='delete'),
]