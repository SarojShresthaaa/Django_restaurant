from rest_framework import serializers
from .models import Category, Food

class CategorySerializers(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    
    def create(self, validated_data):
        category = Category.objects.create(name = validated_data.get('name'))
        return category
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class FoodSerializers(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    
    def create(self, validated_data):
        food = Food.objects.create(**validated_data)
        return food
        