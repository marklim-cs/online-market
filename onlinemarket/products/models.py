from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    inventory = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}, {self.price}"