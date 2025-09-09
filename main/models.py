import uuid
from django.db import models

class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]
    
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

    def __str__(self):
        return self.name
    
    @property
    def dummy(self):
        return
        