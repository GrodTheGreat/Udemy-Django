from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

# from django.utils.text import slugify


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        to=Address, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=False, db_index=True, default="")
    published_countries = models.ManyToManyField(to=Country)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse(viewname="book-detail", kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(value=self.title)
    #     #! super().save() is a requirement!
    #     return super().save(*args, **kwargs)
