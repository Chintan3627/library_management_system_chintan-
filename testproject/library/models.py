from django.db import models

from authapp.models import LibararyUser

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    copies_available = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class BorrowedBook(models.Model):
    student = models.ForeignKey(LibararyUser, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    borrow_date = models.DateField()
    issue_date = models.DateTimeField(auto_now_add =True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.student.username}"
    
    

    