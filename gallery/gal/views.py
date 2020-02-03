from django.shortcuts import render


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
    
    
def _category(request):
    if 'photocategory' in request.GET and request.GET["photocategory"]:
        search_term = request.GET.get("photocategory")
        searched_categories = Image.search_by-category(search_term)
        message = f"{search_term}"
        
        return render(request,'searchcategory.html',{"message":message,"categoryphotos":searched_categories})
    
    else:
        message="You haven't searched for any category"
        return render(request,'searchcategory.html',{"message":message})