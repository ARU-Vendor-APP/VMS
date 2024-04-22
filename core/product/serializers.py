from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404

from core.abstract.serializers import AbstractSerializer
from core.product.models import Product, Category
from core.user.models import User
from core.user.serializers import UserSerializer


class ProductSerializer(AbstractSerializer):

    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='public_id'
    )

    def validated_author(self, value):
        if self.context['request'].user != value:
            raise ValidationError('You cannot add a product for another user')
        return  value

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['edited']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        return rep

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance


class CategorySerializer(AbstractSerializer):
    class Meta:
        model = Category
        fields = '__all__'
