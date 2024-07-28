from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    status = models.BooleanField(default=False, verbose_name="completed")
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"title: {self.title}\nstatus{self.status}"