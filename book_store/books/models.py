from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse(viewname="book-detail", kwargs={"id": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(value=self.title)
        #! super().save() is a requirement!
        return super().save(*args, **kwargs)
