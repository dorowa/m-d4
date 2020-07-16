from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.full_name}"

class Publisher(models.Model):
    name = models.TextField()
    description = models.TextField()
    found_date = models.SmallIntegerField()
    property_type = models.TextField(default="private")
    rating = models.SmallIntegerField(default=0)
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=1, decimal_places=2, max_digits=10)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.title}"

