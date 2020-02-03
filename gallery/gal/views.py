from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    photos = Image.display_photos()
    return render(request,'welcome.html',{"photos":photos}})

def singlephoto(request,photoid):
    try:
        singlephoto=Image.objects.get(id=photoid)
        
    except DoesNotExist:
        raiseHttp404()
    return render(request,'photodetail.html',{"photo":singlephoto})
    
    
def search_category(request):
    if 'photocategory' in request.GET and request.GET["photocategory"]:
        search_term = request.GET.get("photocategory")
        searched_categories = Image.search_by-category(search_term)
        message = f"{search_term}"
        
        return render(request,'searchcategory.html',{"message":message,"categoryphotos":searched_categories})
    
    else:
        message="You haven't searched for any category"
        return render(request,'searchcategory.html',{"message":message})
    
def search_loaction(request):
    if 'photolocation' in request.GET and request.GET["photolocation"]:
        search_term = request.GET.get("photolocation")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request,'searchlocation.html',{"message":message,"locationphotos":searched_locations})
    
    else:
        message="You haven't searched for any location"
        return render(request,'searchlocation.html',{"message":message})