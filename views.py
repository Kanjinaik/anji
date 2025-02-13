from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse
from .models import Room,Customer,Booking
from django.utils import timezone

# Create your views here.
def available_rooms(request):
    rooms=Room.objects.all()
    return render(request,'hotels/availabl_rooms.html',{'rooms':rooms})

def create_customer(request):
    if request.method == 'POST':
        first_name=request.POSt['first_name']
        last_name=request.POST['lat_name']
        email=request.POST['email']
        phone=request.POST['phone']

        customer = Customer(first_name=first_name,last_name=last_name,email=email,phone=phone)
        customer.save()
        return redirect('available_rooms')
    return render(request,'hotel/create_customer.html')
def book_rooms(request):
    room = get_list_or_404(Room)

    if request.method =='POST':
        customer_id = request.POST['customer']
        check_in_date=request.POST['check_in_date']
        check_out_date=request.POST['check_out_date']
        total_amount=room.price_per_night * (timezone.datetime.strptime(check_out_date, '%y-%m-%d')-timezone.datetime.strptime(check_in_date,'%y-%m-%d')).days

        customer = get_list_or_404(Customer)
        Booking = Booking(customer=customer,room=room,check_in_date=check_in_date,check_out_date=check_out_date,total_amount=total_amount)
        Booking.save()

        room.is_available = False
        room.save()

        return HttpResponse(f"Booking confirmed! Total Amount:{total_amount}")
    customer = Customer.objects.all()
    return render(request,'hotels/book_room.html',{'room':room,'customer':customer})
