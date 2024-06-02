from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path (r'^$', views.index, name='index'),
    re_path (r'^album/$', views.AlbumListView.as_view(), name='album'),
    re_path (r'^albums/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album-detail'),
    re_path (r'^author/$', views.AuthorListView.as_view(), name='author'),
    re_path (r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    
]
urlpatterns += [
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [
    re_path(r'^album/create/$', views.AlbumCreate.as_view(), name='album_create'),
    re_path(r'^album/(?P<pk>\d+)/update/$', views.AlbumUpdate.as_view(), name='album_update'),
    re_path(r'^album/(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),
]