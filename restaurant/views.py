from django.shortcuts import render
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializers

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializers(category, many = True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data)
