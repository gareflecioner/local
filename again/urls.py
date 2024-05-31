from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path (r'^$', views.index, name='index'),
    re_path (r'^albums/$', views.AlbumListView.as_view(), name='album'),
    re_path (r'^albums/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album-detail'),
    re_path (r'^author/$', views.AuthorListView.as_view(), name='author'),
    re_path (r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    
]
