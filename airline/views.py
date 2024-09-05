from django.shortcuts import render
from .models import airport,flight,passenger

# Create your views here.
def listofairports(request):
    airports = airport.objects.all()   # select * from airport

    # list(airports)
    return render(request,"airline/listofairports.html",{"airports":list(airports)})
#[{"code":1,"city":"Ahme"},{},{}]


def flight_home(request):
    flights=flight.objects.all()

    return render(request,"airline/FlightHome.html",{"flights":flights})

def flight_details(request,flight_id):
     flightdetail=flight.objects.get(pk=flight_id)

     return render(request,"airline/flightdetail.html",
                   {
                       "flight":flightdetail,
                       "passengers":flightdetail.passengers.all(),
                       #"passenger":passenger.objects.all(flight_id=flight_id),
                    })