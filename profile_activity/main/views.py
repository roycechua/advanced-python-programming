from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request=request,
                  template_name="main/index.html",
                  context={"profile":Profile.objects.all()[0],
                           "job_positions":JobPosition.objects.all})

def send_email(request):
    if request.method == "POST":
        name = request.POST["name"]
        receiver_email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        print(name, receiver_email)

        sender_email = settings.EMAIL_HOST_USER
        subject = 'Hi, I have an inquiry'
        recipient_list = [receiver_email,]
        
        send_mail( subject, message, sender_email, recipient_list )
        
        return redirect('/')
    else:
        return redirect('/')