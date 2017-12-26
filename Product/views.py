# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Product
from serializer import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all();
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ProductDetailedView(APIView):
    def get(selfself,reuest,pk):
        product = Product.objects.get(pk=pk);
        serializer = ProductSerializer(product);
        return Response(serializer.data);
    def put(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({"deleted" : "OK"})