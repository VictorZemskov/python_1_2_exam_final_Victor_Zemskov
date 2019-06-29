from django.contrib import admin
from webapp.models import UserInfo, Author, Book, BookShelf, Review


admin.site.register(UserInfo)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookShelf)
admin.site.register(Review)
