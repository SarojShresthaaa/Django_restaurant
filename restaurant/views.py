from django.shortcuts import render
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializers, FoodSerializers
from rest_framework import status

#Class Based Views
from rest_framework.views import APIView

class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CategoryDetails(APIView):
    
    def get(self, request, id):
        category = Category.objects.get(id = id)
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    
    def put(self, request, id):
        category = Category.objects.get(id = id)
        serializer = CategorySerializers(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        category = Category.objects.get(id=id)
        items = OrderItem.objects.filter(food__category = category).count()
        if items > 0:
            return Response("Data can't be deleted")
        else:
            category.delete()
            return Response("Data is deleted", status.HTTP_204_NO_CONTENT)
        


#--------------------------------------------------------------------------------------------------
# CLASS BASED VIEW FOR FOOD
class FoodList(APIView):
    def get(self, request):
        all_foods = Food.objects.all()
        serializer = FoodSerializers(all_foods, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FoodSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class FoodDetail(APIView):
    def get(self, request, id):
        food = Food.objects.get(id = id)
        serializer = FoodSerializers(food)
        return Response(serializer.data)
    
    def put(self, request, id):
        food = Food.objects.get(id = id)
        serializer = FoodSerializers(food, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        food = Food.objects.get(id = id)
        food.delete()
        return Response("Data is deleted", status.HTTP_204_NO_CONTENT )



#--------------------------------------------------------------------------------------------------
# Function Based Views

# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializers(category, many=True)
#         return Response (serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializers(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response (serializer.data, status=201)
    
# @api_view(['GET', 'DELETE', 'PUT'])  
# def category_details(request, id):
#     category = Category.objects.get(id=id)

#     if request.method == 'GET':
#         serializer = CategorySerializers(category)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = CategorySerializers(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response("Data has been deleted", status.HTTP_204_NO_CONTENT)
        

#--------------------------------------------------------------------------------------------------
# Function based views for FOOD
# @api_view(['GET', 'POST'])
# def food_view(request):
#     if request.method == 'GET':
#         all_foods = Food.objects.all()
#         serializer = FoodSerializers(all_foods, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = FoodSerializers(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

