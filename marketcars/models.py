from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand_name}'

class CarModel(models.Model):
    brand_model = models.CharField(max_length=100)
    brand_category_model = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand_model}'

class Car(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_car = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_year = models.PositiveIntegerField()
    car_mileage = models.PositiveIntegerField()
    car_color = models.CharField(max_length=30)
    car_volume = models.DecimalField(max_digits=10, decimal_places=2)
    is_have = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return (f'{self.brand_model} - '
                f'{self.brand_car} - '
                f'{self.car_year} - '
                f'{self.car_color} - '
                f'{self.car_volume} - '
                f'{self.description} -')