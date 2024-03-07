from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
    
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class FreeTrial(models.Model):
    duration = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.duration
    
class Pricing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.price

class Product(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=2083)
    description = models.TextField()
    video_url = models.CharField(max_length=2083)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    link = models.CharField(max_length=2083)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    file = models.FileField(upload_to='uploads/')
    statistics = models.JSONField()
    report_file = models.FileField(upload_to='uploads/')
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    free_trial = models.ForeignKey(FreeTrial, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name