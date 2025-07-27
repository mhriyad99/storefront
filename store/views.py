from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store.models import Product
from store.serializers import ProductSerializer

@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def product_detail(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)
        serialize = ProductSerializer(product, context={'request': request})
        return Response(serialize.data)
    
    elif request.method == 'POST':
        serialize = ProductSerializer(data=request.data)
        return Response('ok')

@api_view()
def collection_detail(request, pk):
    return Response('ok')