
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from super_types.models import SuperType


# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):

    if request.method == 'GET':
        
        type_param = request.query_params.get('type')
        if type_param:
            query_set = Super.objects.filter(super_type__type = type_param)
            serializer = SuperSerializer(query_set, many = True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        
        super_types = SuperType.objects.all()
        custom_response_dictionary = {}
        for type in super_types:
            supers = Super.objects.filter(super_type = type.id)
            super_serialzier = SuperSerializer(supers, many = True)

            custom_response_dictionary[type.type] = {
                "Supers": super_serialzier.data
            }

        return Response(custom_response_dictionary)
        
    if request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk):
    result = get_object_or_404(Super, pk = pk)

    if request.method == 'GET':
        serializer = SuperSerializer(result)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(result, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        result.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
