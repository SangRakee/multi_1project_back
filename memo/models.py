from django.db import models
from user.models import User
from book.models import Book, BookArticle


# Create your models here.

class Memo(models.Model):
    objects = models.Manager()
    memoId = models.AutoField(primary_key=True)
    memoTitle = models.CharField(max_length=250)
    memoContent = models.TextField()
    memoDate = models.DateTimeField(auto_now=True)
    memoImg = models.CharField(max_length=250, null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    articleId = models.ForeignKey(BookArticle, on_delete=models.SET_DEFAULT, default='bookshelf')
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
