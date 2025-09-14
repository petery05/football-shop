from django.urls import path
from main.views import show_main, show_product, create_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('product/<str:id>', show_product, name='show_product'),
    path('create-product/', create_product, name='create_product'),
]