from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is homepage')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This is about page')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('This is services page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, mobile = mobile, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted.')
    return render(request, 'contact.html')
    #return HttpResponse('This is contact page')


