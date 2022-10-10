from unittest import result
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerialzier

# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):

    if request.method == 'GET':
        query_set = Super.objects.all()
        serializer = SuperSerialzier(query_set, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = SuperSerialzier(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def supers_detail(request, pk):
    result = get_object_or_404(Super, pk = pk)

    if request.method == 'GET':
        serializer = SuperSerialzier(result)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerialzier(result, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        result.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
