from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Company(models.Model):
    name_ar = models.CharField(max_length=100, null=True)
    name_en = models.CharField(max_length=100, null=True)
    name_fr = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logo/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=225, null=True)
    fb = models.URLField(null=True)
    twitter = models.URLField(null=True)
    google = models.URLField(null=True)

    def __str__(self):
        return self.name_en


class Category(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_ar = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_fr = models.CharField(max_length=255)

    def __str__(self):
        return self.name_en


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_ar = models.CharField(max_length=255, null=True)
    name_en = models.CharField(max_length=255, null=True)
    name_fr = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cover = models.ImageField(upload_to='cover/')
    description_ar = models.TextField(null=True)
    description_en = models.TextField(null=True)
    description_fr = models.TextField(null=True)

    def __str__(self):
        return self.name_en


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'review #{self.id} by {self.owner}'


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'order {self.id} by {self.owner}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(null=False)
    size = models.CharField(max_length=3, null=True)
