from rest_framework import serializers

from .models import Product, Category, Pricing, FreeTrial, Review, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class FreeTrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeTrial
        fields = '__all__'

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    pricing = PricingSerializer()
    free_trial = FreeTrialSerializer()
    review = ReviewSerializer()
    class Meta:
        model = Product
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'