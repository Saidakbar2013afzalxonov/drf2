from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, null=False)
    price = models.PositiveBigIntegerField(blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name