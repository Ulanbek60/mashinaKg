from .models import Car
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class ProductTranslationOptions(TranslationOptions):
    fields = ('brand_name', 'description','car_color')