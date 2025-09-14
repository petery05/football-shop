from django.forms import ModelForm
from main.models import Shop

class ProductForm(ModelForm):
    class Meta:
        model = Shop
        fields = {"name", "price", "description", "category", "thumbnail", "is_featured", "brand"}