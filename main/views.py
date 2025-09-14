from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Shop

# Create your views here.
def show_main(request):
    context = {
        'project' : 'Football Shop',
        'npm' : '2406432910',
        'name': 'Peter yap',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main.show_main')
    
    context = {'form':form}
    return render(request, "create_product.html", context)

def show_product(request):
    product = get_object_or_404(Shop,pk=id)
    
    context = {
        'product':product
    }

    return render(request,"product_detail.html",context)

