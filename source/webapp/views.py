from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import Author, Book
from django.http import HttpResponseRedirect, JsonResponse
from webapp.forms import AuthorForm, BookForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

    def get_queryset(self):
        return Author.objects.filter(is_deleted=False)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_update.html'
    success_url = reverse_lazy('author_list')


def soft_delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.is_deleted = True
    author.save()
    return redirect('author_list')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        return Book.objects.filter(is_deleted=False)


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('author_list')


def soft_delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.is_deleted = True
    book.save()
    return redirect('book_list')