from django.shortcuts import render,redirect
from .models import Contact,Product
from django.contrib import messages
from math import ceil


def index(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    print(catprods)
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))           #logic to display the products on index fil
        allProds.append([prod,range(1,nSlides),nSlides])        
    params={'allProds':allProds}
    return render(request,"index.html",params)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")

        myquery = Contact(name=name, email=email, desc=desc, phonnumber=pnumber)
        myquery.save()

        messages.info(request, "We will get back to you soon")
        return redirect('contact')  # Redirect to the same view after form submission

    return render(request, "contact.html")



def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")


def order(request):
    return render(request,"order.html")

def checkout(request):
    return render(request,"checkout.html")



"""Not:ceil:ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result. Tip: To round a number DOWN to the nearest integer, look at the math"""""