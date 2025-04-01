from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(
        max_length=50, blank=True, null=False, default=""
    )
    email = models.EmailField(
        max_length=254, blank=True, null=False, default=""
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=250)
    image_name = models.FilePathField()
    date = models.DateField()
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=Tag)

    def __str__(self):
        return f"{self.title} - {self.author.get_full_name()}"
