from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path (r'^$', views.index, name='index'),
    re_path(r'^profile/$', views.profile,name='profile'),
    re_path (r'^album/$', views.AlbumListView.as_view(), name='album'),
    re_path (r'^albums/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album-detail'),
    re_path (r'^author/$', views.AuthorListView.as_view(), name='author'),
    re_path (r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    
]
urlpatterns += [
    re_path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    re_path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    re_path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
urlpatterns += [
    re_path('album/create/', views.AlbumCreate.as_view(), name='album-create'),
    re_path('album/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),
    re_path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]