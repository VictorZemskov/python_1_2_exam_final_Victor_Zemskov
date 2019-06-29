"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from webapp.views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, soft_delete_author,\
                         BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, UserDetailView
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create', AuthorCreateView.as_view(), name='author_create'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),
    path('authors/<int:pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete', soft_delete_author, name='author_delete'),
    path('', BookListView.as_view(), name='book_list'),
    path('books/create', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)