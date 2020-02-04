from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def welcome(request):
    photos = Image.display_photos()
    return render(request,'all-photos/welcome.html',{"photos":photos})

def singlephoto(request,photoid):
    try:
        singlephoto=Image.objects.get(id=photoid)
        
    except DoesNotExist:
        raiseHttp404()
    return render(request,'all-photos/photodetail.html',{"photo":singlephoto})
    
    
def search_category(request):
    if 'photocategory' in request.GET and request.GET["photocategory"]:
        search_term = request.GET.get("photocategory")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request,'all-photos/searchcategory.html',{"message":message,"categoryphotos":searched_categories})
    
    else:
        message="You haven't searched for any category"
        return render(request,'searchcategory.html',{"message":message})
    
def search_location(request):
    if 'photolocation' in request.GET and request.GET["photolocation"]:
        search_term = request.GET.get("photolocation")
        searched_location = Image.filter_by_location(search_term)
        message = f"{search_term}"
        
        return render(request,'all-photos/searchlocation.html',{"message":message,"locationphotos":searched_location})
    
    else:
        message="You haven't searched for any location"
        return render(request,'all-photos/searchlocation.html',{"message":message})