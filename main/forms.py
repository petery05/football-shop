from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = {"name", "price", "description", "category", "thumbnail", "is_featured", "brand", "sale"}

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)

    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return strip_tags(brand)
    
    def clean_sale(self):
        sale = self.cleaned_data["sale"]
        return strip_tags(sale)
