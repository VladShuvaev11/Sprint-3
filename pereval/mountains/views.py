from rest_framework import viewsets
from django_filters import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import MountainSerializer


class MountainsViewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
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