from django.db import models

# create your models here
class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()  # Fixed the missing parentheses

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    status = models.BooleanField(default=False, verbose_name="completed")
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)  # Allows null values

    def __str__(self):
        return f"title: {self.title}\nstatus: {self.status}"  # Added space after 'status'
