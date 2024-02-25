from django.contrib import admin

# Register your models here.

from .models import Category, FreeTrial, Pricing, Product, Review

admin.site.register(Category)
admin.site.register(FreeTrial)
admin.site.register(Pricing)
admin.site.register(Product)
admin.site.register(Review)