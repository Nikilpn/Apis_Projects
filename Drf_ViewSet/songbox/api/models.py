from django.db import models

# Create your models here.


from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    run_time = models.IntegerField()  # Assuming runtime is stored in minutes
    language = models.CharField(max_length=200)
    year = models.CharField(max_length=200)


    def __str__(self):
        return self.title
