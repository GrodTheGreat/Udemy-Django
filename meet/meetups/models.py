from django.db import models


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.title} - {self.slug}"
