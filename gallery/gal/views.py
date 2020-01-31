from django.shortcuts import render

# Create your views here.
def welcome(request):
    photos = Image.display_photos()
    return render(request,'welcome.html'})
    