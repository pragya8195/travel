from django.http import HttpResponse
from django.shortcuts import render
from .models import place, person


# Create your views here.
#def home(request):
#    return render(request,"home.html")
#def about(request):
#    return render(request,"about.html")
#def contact(request):
#    return HttpResponse("contact page")
#def details(request):
#    return HttpResponse("details page")
#def thanks(request):
 #   return HttpResponse("thank you")
def demo(request):
    obj=place.objects.all()
    obj1 = person.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})




