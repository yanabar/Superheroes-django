from django.db import models

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def _str_(self):
        return self.name
