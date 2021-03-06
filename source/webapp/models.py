from django.db import models
from django.contrib.auth.models import User


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', verbose_name='Пользователь')
    name = models.CharField(max_length=255, verbose_name='Ф.И.О.')
    email = models.EmailField(max_length=50, verbose_name="Почта")
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ф.И.О.')
    birth_date = models.DateField(null=True, blank=True, verbose_name='дата рождения')
    death_date = models.DateField(null=True, blank=True, verbose_name='дата смерти')
    biography = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Биография')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Автор')
    year_publishing = models.CharField(max_length=255, verbose_name='Год издания')
    file = models.FileField(null=True, blank=True, verbose_name='Файл')
    cover = models.ImageField(null=True, blank=True, verbose_name='Обложка')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.name


class BookShelf(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='book_shelfs', verbose_name='Пользователь')
    book = models.ManyToManyField(Book, related_name='book_shelfs', verbose_name='Книги')
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return "книжная полка пользователя %s" % (self.user)


class Review(models.Model):
    book = models.ManyToManyField(Book, related_name='reviews', verbose_name='Книги')
    user = models.ManyToManyField(UserInfo, related_name='reviews', verbose_name='Пользователи')
    сontent = models.TextField(max_length=2000, verbose_name='Отзыв')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return "Отзыв на книгу %s" % (self.book)




