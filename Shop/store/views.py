from django.shortcuts import render,resolve_url


# Create your views here.

def store_info(request):
    return render(request,'index.html')