from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,OrderItem,Customer
from django.core import exceptions
from django.db.models import Value,F,Func

# Create your views here.

def say_hello(request):
    try:
        # query_set=Product.objects.all()[:5]
        query_set=Product.objects.values("id","title")[:5] 
        query_set=Product.objects.values_list("id","title")[:5] 
        query_set=OrderItem.objects.values("product_id").distinct()
        query_set=Product.objects.filter(id__in=OrderItem.objects.values("product_id").distinct())
        query_set=Product.objects.select_related("collection").all()
        query_set=Customer.objects.annotate(full_name=Func(F('first_name'),Value(''),F('last_name'),function='CONCAT'))


        return render(request,"hello.html",{'name':"santhosh", "products":list(query_set)})
        # print(list(query_set))
    except:
        exceptions.ObjectDoesNotExist
        print("error")


    return HttpResponse("hi")