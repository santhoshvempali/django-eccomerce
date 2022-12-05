from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product 
from django.core import exceptions

# Create your views here.

def say_hello(request):
    try:
        query_set=Product.objects.get(pk=0)
        for data in query_set:
            print(data)
    except:
        exceptions.ObjectDoesNotExist
        pass


    return HttpResponse("hi")