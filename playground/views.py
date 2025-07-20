from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Prefetch, Value, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min, Max, Avg
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, OrderItem, Order, Collection
from tags.models import Tag, TaggedItem

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Riyad'})
