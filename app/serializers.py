from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','description','updated_at','created_at','id']
        read_only_fields = ['id','created_at','updated_at']