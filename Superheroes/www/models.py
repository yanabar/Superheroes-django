from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True)
    responsibilities = models.CharField(max_length=1000, default='')
    bio = models.CharField(max_length=1000, default='')
    twitter = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(default = timezone.now)


    def save(self, *args, **kwargs):
        if not self.pk: #has this been already created?
            self.slug = slugify(self.name)
        super(Superhero, self).save(*args, **kwargs)


    def _str_(self):
        return self.name
