from django.shortcuts import render
from .models import *
# from rest_framework.views import APIView
# from .serializers import *
# from rest_framework.response import Response


def login(request):
    pa = Product_mst.objects.all()
    return render(request,'product.html', {'all_pro':pa})

def add(request):
    Product_sub_cat.objects.create(
        Product_prize = request.POST['prize'],
        Product_img = request.FILES['image'],
        Product_model = request.POST['model'],
        Product_ram = request.POST['ram'],
        Product_name = Product_mst.objects.get(Product_Name = request.POST['name'])
        )
    return render(request, 'delete.html')
    
def update(request):
    return render(request, 'update.html')

def delete(request):
    global paa
    paa = Product_sub_cat.objects.all()
    return render(request,'delete.html', {'all_pro':paa})
def delete_item(request,pk):
    fun = Product_sub_cat.objects.get(id=pk)
    fun.delete()
    return render(request,'delete.html',{'all_pro':paa})

def update(request, pk):
    if request.method == "GET":
        updated_products = Product_sub_cat.objects.get(id = pk)
        return render(request, 'update.html', {'pro':updated_products})
    else:
        updated_products = Product_sub_cat.objects.get(id= pk)
        updated_products.product_model = request.POST['model']
        updated_products.product_ram = request.POST['ram']
        updated_products.product_image = request.FILES['image']
        updated_products.product_price = request.POST['price']
        updated_products.save()
        return render(request, 'update.html', {'pro':updated_products})
    
def product_manager(request):
    all_products = Product_sub_cat.objects.all()
    return render(request, 'product_manager.html', {'pro':all_products})

