from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(
        max_length=100, blank=True, null=False, default=""
    )
    email = models.EmailField(
        max_length=254, blank=True, null=False, default=""
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        to=Author, on_delete=models.SET_NULL, related_name="posts", null=True
    )
    tags = models.ManyToManyField(to=Tag)

    def __str__(self):
        return f"{self.title} - {self.author.get_full_name()}"


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(max_length=250)
    text = models.TextField(max_length=400)
