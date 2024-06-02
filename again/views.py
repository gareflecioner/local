from django.http import Http404
from django.shortcuts import render
from django.views import generic


# Create your views here.

from .models import Album, Author, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_albums=Album.objects.all().count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    return render(
        request,
        'index.html',
        context={'num_albums':num_albums,'num_authors':num_authors,'num_visits':num_visits },
    )

class AlbumListView(generic.ListView):
    model = Album
    context_object_name = 'my_album_list'   # ваше собственное имя переменной контекста в шаблоне
    template_name = 'again/albumList.html'  # Определение имени вашего шаблона и его расположения

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AlbumListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'again/albumDetail.html'  # Определение имени вашего шаблона и его расположения
    
def album_detail_view(request,pk):
    try:
        album_id=Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'again/albumDetail.html',
        context={'album':album_id,}
    )



class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'my_author_list'   # ваше собственное имя переменной контекста в шаблоне
    template_name = 'again/authorList.html'  # Определение имени вашего шаблона и его расположения

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['Album'] = Album.objects.all()
        return context

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'again/authorDetail.html'  # Определение имени вашего шаблона и его расположения
    
def author_detail_view(request,pk):
    try:
        author_id=Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'again/authorDetail.html',
        context={'author':author_id,}
    )


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author,Album

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author')




class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['title','genre']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('album')
