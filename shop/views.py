from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact , Order , OrderUpdate
from  math import ceil
import json 

def index(request):
    allprods = []
    allcat = Product.objects.values('categary', 'id')
    cats = {items['categary'] for items in allcat}
    for cat in cats:
        prods=Product.objects.filter(categary=cat)
        n = len(prods)
        noslide = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prods ,range(1,noslide), noslide])

    dist={'allprods':allprods}
    return render(request,'shop/index.html',dist)


def searchMatch(query,item):

    if query in item.product_name.lower() or query in item.desc.lower() or query in item.categary.lower():
        return True
    else:
        return False
def search(request):
    query=request.GET.get('search')
    allprods = []
    allcat = Product.objects.values('categary', 'id')
    cats = {items['categary'] for items in allcat}
    for cat in cats:
        prodtemp = Product.objects.filter(categary=cat)
        prods=[item for item in prodtemp if searchMatch(query,item)]
        n = len(prods)
        noslide = n // 4 + ceil((n / 4) - (n // 4))
        if len(prods) != 0:
            allprods.append([prods, range(1, noslide), noslide])
    dist = {'allprods': allprods,'msg':''}
    if len(allprods) == 0 or len(query)<4:
        dist={'msg':'Muhammad Ali'}

    return render(request, 'shop/search.html', dist)


def about(request):
    return render(request,'shop/about.html')
def contact(request):
    thank=False
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        cont=Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
        thank=True

    return render(request,'shop/contact.html',{'thank':thank})
def tracker(request):
     if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
     
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({'status':'sucess' ,'updates': updates, 'itemJson': order[0].items_json } ,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitems"}')
        except Exception as e: 
            return HttpResponse("{'status':'error'}")

     return render(request, 'shop/tracker.html')
        

def productVeiw(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodview.html',{'product':product[0]}) 
def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') +" " +  request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code= request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order( items_json=items_json, order_name=name, email=email ,city=city , state = state ,
                       address=address, zip_code=zip_code,amount=amount , phone=phone )
        order.save()
        update = OrderUpdate(order_id=order.order_id , update_desc = " your order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})


    return render(request,'shop/checkout.html')