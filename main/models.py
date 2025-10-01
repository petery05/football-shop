import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('bag', 'BAG'),
        ('jersey', 'JERSEY'),
        ('exclusive', 'Exclusive'),
        ('boots', 'Boots'),
        ('accessories', 'Accessories'),
        ('hoodie', 'Hoodie'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, default=0, decimal_places=1)
    total_purcased = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100)
    sale = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.total_purcased > 10
    
    @property
    def after_discount(self):
        return self.price - (self.price*self.sale//100)
