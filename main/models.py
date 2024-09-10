from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    rating = models.DecimalField(
    max_digits=2, 
    decimal_places=1, 
    null=True, 
    blank=True, 
    default=1.0,
    validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name