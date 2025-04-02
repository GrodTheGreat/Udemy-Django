from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=5),
        ]
    )
