from rest_framework import viewsets, permissions
from .models import Brand, CarModel, Car
from .serializers import BrandSerializer, CarModelSerializer, CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter
from rest_framework.filters import SearchFilter


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter    ]
    filterset_class = CarFilter
    search_fields = ['brand_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
