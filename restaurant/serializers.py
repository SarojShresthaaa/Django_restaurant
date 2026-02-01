from rest_framework import serializers
from .models import Category, Food
from rest_framework.serializers import ModelSerializer


# Using .Serializer
# class CategorySerializers(serializers.Serializer):
#     name = serializers.CharField()
#     id = serializers.IntegerField(read_only=True)
    
#     def create(self, validated_data):
#         category = Category.objects.create(name = validated_data.get('name'))
#         return category
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

# Using .ModelSerializer
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


#--------------------------------------------------------------------------------------------------
# class FoodSerializers(serializers.Serializer):
#     name = serializers.CharField()
#     id = serializers.IntegerField(read_only=True)
#     description = serializers.CharField()
#     price = serializers.IntegerField()
#     category = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all()
#     )
    
#     def create(self, validated_data):
#         food = Food.objects.create(**validated_data)
#         return food
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.category = validated_data.get('category', instance.category)
#         instance.save()
#         return instance

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'price', 'category']