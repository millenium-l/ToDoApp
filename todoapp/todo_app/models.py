from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.pk}. {self.first_name} {self.last_name}"
    # self.pk means primary key eg 1 