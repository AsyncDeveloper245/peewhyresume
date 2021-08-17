from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import UserMessage
# Create your views here.


def homepageView(request):
    if request.method == "GET":
        return render(request,'index.html')
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        name = request.POST.get('name')

        try:
            userMessage = UserMessage.objects.create(subject=subject,message=message,email=email,name=name)
            userMessage.save()
            
            return HttpResponse("Message Sent Successfully")
        except:
            return HttpResponse("Email Not Sent")


        print(email)

