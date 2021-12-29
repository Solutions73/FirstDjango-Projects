from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.

def index(request):
    context = {
       'variable1': 'this is the value of the variable',
       'variable2': 'value of the variable'
    }
    # messages.success(request, "this is a test message") need to delete this it was just to see how it looks
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")


def about(request):
    return render(request, 'about.html')

    #return HttpResponse("This is aboutpage")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is servicespage")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Form submitted succesfully!!')
    return render(request, 'contact.html')
    #return HttpResponse("This is contactpage")
