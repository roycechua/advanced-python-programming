from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="home/home.html",
                  context={"training":Training.objects.all})
                #  Training.objects.all or Training.objects.all() 