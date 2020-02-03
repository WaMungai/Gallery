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
    