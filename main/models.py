# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('NEW ARRIVALS', 'NEW ARRIVALS'),
        ('EXCLUSIVE', 'EXCLUSIVE'),
        ('SALE', 'SALE'),
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN'),
        ('KIDS', 'KIDS'),
        ('COMING SOON', 'COMING SOON'),
        ('BRAND', 'BRAND'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='NEW ARRIVALS')
    thumbnail = models.URLField(blank=True, null=True)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()