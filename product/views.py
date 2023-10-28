from django.shortcuts import render
from product.models import product_model
from django.http import HttpResponse
# Create your views here.


def create_view(request, pname, desc, price, discount=5):
    res = product_model.objects.create(
        pname=pname, price=price, desc=desc, discount=discount)
    return HttpResponse("Product is successfully stored")


def list_view(request):
    res = product_model.objects.all()
    return render(request=request, template_name='list.html', context={'data': res})


def details_view(request, pk):
    try:
        res = product_model.objects.get(pid=pk)
    except:
        res = None
    return render(request=request, template_name='details.html', context={'data': res, 'id': pk})


def update_view(request, pk, value):
    res = product_model.objects.get(pid=pk)
    res.price = value
    res.save()
    return HttpResponse(f"product id {res.pid} successfully update")


def delete_view(request, pk):
    res = product_model.objects.filter(pid=pk).delete()
    return HttpResponse(f"product id {pk} successfully delete")


def register_view(request):
    if request.method == 'POST':
        res = product_model.objects.create(
            pname=request.POST['name'], price=request.POST['price'], desc=request.POST['desc'], discount=request.POST['discount'])
        return HttpResponse("Product is successfully stored")
        
    return render(request=request, template_name='create.html')
