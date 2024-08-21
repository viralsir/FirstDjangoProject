from django.shortcuts import render
from .models import airport

# Create your views here.
def listofairports(request):
    airports = airport.objects.all()   # select * from airport

    # list(airports)
    return render(request,"airline/listofairports.html",{"airports":list(airports)})
#[{"code":1,"city":"Ahme"},{},{}]
