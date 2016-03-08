from django.conf.urls import include, url
from django.contrib import admin
from news import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    # url(r'^add$', views.AddDate.as_view(), name='add'),
    # url(r'^search$', views.SearchDate.as_view(), name='search'),
    # url(r'^results$', views.SearchDate.as_view(), name='results'),
]