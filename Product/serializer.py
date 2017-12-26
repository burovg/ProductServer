from rest_framework import serializers
from models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'Name', 'Description', 'Price', 'InStock', 'id'
        #fields = '__all__'


