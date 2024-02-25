from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Category, Pricing, FreeTrial, Review
from .serializers import ProductSerializer, CategorySerializer, PricingSerializer, FreeTrialSerializer, ReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class FreeTrialViewSet(viewsets.ModelViewSet):
    queryset = FreeTrial.objects.all()
    serializer_class = FreeTrialSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

