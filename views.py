from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Create your views here.
def home(request):
    if request.method == 'POST':
        origin_address = request.POST.get('origin')
        destination_address = request.POST.get('destination')
        geolocator = Nominatim(user_agent="location_app")
        origin = geolocator.geocode(origin_address)
        destination = geolocator.geocode(destination_address)

        if origin and destination:
            origin_coords = (origin.latitude,origin.longitude)
            destination_coords = (destination.latitude,destination.longitude)

            distance = geodesic(origin_coords,destination_coords).km
            context = {
                'origin':origin_address,
                'destination':destination_address,
                'distance':distance,
                'origin_lat':origin.latitude,
                'destination_lat':destination.latitude,
                'destination_lon':destination.longitude,
            }
            return render(request,'navigation/home.html',context)
        else:
            context={'error':"couldn't geocode one of the address."}
            return render(request,'home.html',context)
    return render(request,'navigation/home.html')
        

