from django_filters import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'brand_car': ['exact'],
            'brand_model': ['exact'],
            'car_year': ['exact'],
            'price': ['gt', 'lt'],
        }