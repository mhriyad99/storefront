from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Prefetch, Value, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min, Max, Avg
from store.models import Product, Customer, OrderItem, Order

# Create your views here.
def say_hello(request):
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )

    queryset = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, 'hello.html', {'name': 'Riyad', 'result': list(queryset)})
