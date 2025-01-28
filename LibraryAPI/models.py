from django.db import models

# Create your models here.

# create a model for a book
class Book(models.Model):
    # get the primary key from the database    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=13)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    summary = models.TextField()
    # save the time each time a book updates, not just when it was created
    created_at = models.DateTimeField(auto_now_add=True)
    # if the book is available use bool
    availability = models.BooleanField(default=True)

    # return the title
    def __str__(self):
        return self.title
