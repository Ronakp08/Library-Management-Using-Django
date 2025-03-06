from django.db import models

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    ISBN = models.BigIntegerField(unique=True)

    def __str__(self):
        return f"{self.Title} - ISBN: {self.ISBN}"


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=200)

    def __str__(self):
        return self.Username


class BorrowedBook(models.Model):
    BorrowedID = models.AutoField(primary_key=True)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField()

    def __str__(self):
        return f"Borrowed {self.BookID.Title} by {self.UserID.Username}"
