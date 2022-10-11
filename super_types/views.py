
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializer import SuperTypeSerializer
from super_types.models import SuperType


@api_view(['GET','POST'])
def super_types_list(request):
    if request.method == 'GET':
        query_set = SuperType.objects.all()
        serializer = SuperTypeSerializer(query_set,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def super_type_detail(request,pk):
    query = get_object_or_404(SuperType,pk = pk)

    if request.method == 'GET':
        serializer = SuperTypeSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(query,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)