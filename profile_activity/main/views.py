from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request=request,
                  template_name="main/index.html",
                  context={"profile":Profile.objects.all()[0],
                           "job_positions":JobPosition.objects.all})