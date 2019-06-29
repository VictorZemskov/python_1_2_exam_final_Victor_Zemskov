from django import forms
from webapp.models import Author, Book, BookShelf, Review

# class ProjectSearchForm(forms.Form):
#     project_name = forms.CharField(max_length=50, required=False, label="Имя проекта")


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['is_deleted']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['is_deleted']


class BookShelfForm(forms.ModelForm):
    class Meta:
        model = BookShelf
        exclude = ['is_deleted']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['is_deleted']