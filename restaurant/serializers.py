from rest_framework import serializers
from .models import Category

class CategorySerializers(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    
    def create(self, validated_data):
        category = Category.objects.create(name = validated_data.get('name'))
        return category
    