from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,related_name="product", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.IntegerField()

    description = models.TextField()
    is_sold = models.BooleanField(default=False)
    stock = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="product", on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


# Create your models here.
