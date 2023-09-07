import django_filters
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from .models import *
from .serializers import MountainSerializer






class MountainsViewSet(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user__email']


@api_view(['POST'])
def submit_data(request):
    serializer = MountainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_data(pk):
    try:
        perevals = Mountain.objects.get(pk=pk)
    except Exception:
        return Response(status=404)
    serializer = MountainSerializer(perevals)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_data(request, pk):
    try:
        mountain = Mountain.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'state': 0, 'message': 'Перевал не существует'}, status=status.HTTP_404_NOT_FOUND)

    if mountain != 'NEW':
        return Response({'state': 0, 'message': 'Редактировать данные об объекте нельзя'})

    serializer = MountainSerializer(mountain, data=request.data )
    if serializer.is_valid():
        serializer.save()
        return Response({'state': 1, 'message': 'Успешно'})
    return Response({'state': 0, 'message': 'Ошибка'})


class MountainsList(ListAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
