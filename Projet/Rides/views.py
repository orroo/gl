from django.shortcuts import render, get_object_or_404, redirect

from .forms import RideForm
import random

from django.utils import timezone

from django.contrib import messages
from .models import Ride, Reservation
from django.shortcuts import render
from .models import Ride
import random

from django.contrib.auth.models import User
from .forms import RideForm

from django.core.paginator import Paginator


from django.db.models import Q  # Import Q for complex queries
from django.contrib.auth.decorators import login_required


def ride_list(request):
    # Get search and sort parameters from the request
    search_query = request.GET.get('q')
    sort_option = request.GET.get('sort')

    # Start with all rides that have available seats
    rides = Ride.objects.filter(available_seats__gt=0)

    # Apply search filter if a query is provided
    if search_query:
        rides = rides.filter(
            Q(destination__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Apply sorting based on the selected option
    if sort_option == 'price_asc':
        rides = rides.order_by('price')
    elif sort_option == 'price_desc':
        rides = rides.order_by('-price')
    elif sort_option == 'seats_desc':
        rides = rides.order_by('-available_seats')
    elif sort_option == 'date_asc':
        rides = rides.order_by('departure_time')
    elif sort_option == 'date_desc':
        rides = rides.order_by('-departure_time')

    # Add random images to rides
    images = [
        '/static/img/car-1.png',
        '/static/img/car-2.png',
        '/static/img/car-3.png',
        '/static/img/car-4.png',
    ]
    for ride in rides:
        ride.image = random.choice(images)

    # Pagination logic
    paginator = Paginator(rides, 6)  # Show 8 rides per page
    page_number = request.GET.get('page')  # Get the page number from the URL query parameter
    page_obj = paginator.get_page(page_number)  # Get the page object

    # Render the ride list template with pagination
    return render(request, 'trajet/rides_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_option': sort_option
    })

@login_required
def ride_detail(request, pk):
    """View to display ride details."""
    ride = get_object_or_404(Ride, pk=pk)
    return render(request, 'trajet/ride_detail.html', {'ride': ride})




def reserve_ride(request, pk):
    # Get the ride instance
    ride = get_object_or_404(Ride, pk=pk)
    
    # Check if there are available seats
    if ride.available_seats < 1:
        messages.error(request, "No seats available for this ride.")
        return redirect('ride_detail', pk=pk)
    
    # Reserve the ride
    Reservation.objects.create(
        user_id=1,  # Assuming user ID is 1 (replace with actual user logic)00000000000000000000000000000000000000000000000000000000000000000000
        ride=ride,
        reservation_date=timezone.now(),
    )
    
    # Reduce available seats by 1
    ride.available_seats -= 1
    ride.save()

    # Redirect to the "My Reservations" page or ride list
    messages.success(request, "Ride reserved successfully!")
    return redirect('my_reservations')



@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user_id=1)  # Replace with actual user logic
    return render(request, 'trajet/my_reservations.html', {'reservations': reservations})
# In your views.py

def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    ride = reservation.ride
    
    # Increment available seats when the reservation is canceled
    ride.available_seats += 1
    ride.save()
    
    # Delete the reservation
    reservation.delete()
    
    messages.success(request, "Reservation canceled and seat is now available!")
    return redirect('my_reservations')


@login_required
def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)  # Do not save to the database yet
            ride.owner = request.user       # Set the owner to the logged-in user
            ride.save()                     # Now save to the database
            return redirect('/rides/')      # Redirect to the rides list page after saving
            print("YESSSSSS")
        else:
            return render(request, 'trajet/create_ride.html', {'form': form})  # Re-render the form with errors
    else:
        form = RideForm()
    return render(request, 'trajet/create_ride.html', {'form': form})



def edit_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    
    if request.method == 'POST':
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            return redirect('my_rides')  # Redirect to the list of rides
    else:
        form = RideForm(instance=ride)
    
    return render(request, 'trajet/edit_ride.html', {'form': form})







def delete_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    
    if request.method == 'POST':
        ride.delete()
        return redirect('my_rides')  # Redirect to the list of rides after deletion
    
    return render(request, 'trajet/confirm_delete.html', {'ride': ride})





@login_required
def my_rides(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('options')   # For testing purposes
    
    user_rides = Ride.objects.filter(owner=user)
    
    return render(request, 'trajet/my_rides.html', {'user_rides': user_rides})
