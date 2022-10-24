from django.shortcuts import render

# Create your views here.

# Returns the index page to the home page.
def index(request):
    return render(request, "index.html")

def online_cv(request):
    return render(request, "cv.html")

def yum_yum(request):
    return render(request, "yum_yum.html")