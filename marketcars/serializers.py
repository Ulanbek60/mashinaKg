from rest_framework import serializers
from .models import Brand, CarModel, Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','brand_name','brand_car',
                  'brand_model','price','car_year','car_mileage',
                  'car_color','is_have','car_volume','description',
                  'video','image']