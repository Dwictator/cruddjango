from django.shortcuts import render, redirect
from.models import inputProduct
from django.contrib import messages

def createView(request):
    InputProduct = inputProduct.objects.all()
    return render(request,'create.html',{'InputProduct':InputProduct})

def store(request):
    InputProduct = inputProduct()

    InputProduct.productname = request.POST.get('productname')
    InputProduct.productcategory = request.POST.get('productcategory')
    InputProduct.productdescription = request.POST.get('productdescription')
    InputProduct.productstock = request.POST.get('productstock')
    InputProduct.save()
    messages.success(request, "Product Added Successfully")
    return redirect('/create')

def index(request):
    InputProduct = inputProduct.objects.all()
    return render(request, 'create.html',{'InputProduct':InputProduct})

def viewProduct(request,pk):
   viewProduct = inputProduct.objects.get(id = pk)
   return render(request, 'view.html',{'viewProduct':viewProduct})

def deleteProduct(request, pk):
    InputProduct = inputProduct.objects.get(id = pk)
    InputProduct.delete()
    messages.success(request, "Product Deleted Successfully")
    return redirect('/')

def updateView(request,pk):
    InputProduct = inputProduct.objects.get(id = pk)
    return render(request,'edit.html',{'InputProduct':InputProduct})

def update(request,pk):
    
    InputProduct = inputProduct.objects.get(id = pk)
    InputProduct.productname = request.POST.get('productname')
    InputProduct.productcategory = request.POST.get('productcategory')
    InputProduct.productdescription = request.POST.get('productdescription')
    InputProduct.productstock = request.POST.get('productstock')
    InputProduct.save()
    messages.success(request, "Product Added Successfully")
    return redirect('/create')
    