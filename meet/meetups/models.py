from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} ({self.address})"


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(
        to=Location, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.title} - {self.slug}"
