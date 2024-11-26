from django.shortcuts import render, get_object_or_404, redirect
from .models import Avis
from .forms import AvisForm
from userapp.models import user
from Rides.models import Ride
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def avis_list(request):
    # Check if the filter parameter exists in the request
    sort_by_rating = request.GET.get('sort_by', None)
    
    if sort_by_rating == 'rating_desc':
        avis = Avis.objects.filter(approved=True).order_by('-rating')  # Most rated first
    else:
        avis = Avis.objects.filter(approved=True)  # Default order
    
    # Precompute stars and check for bad words in the view for each review
    bad_words = [
        "connard", "salaud", "enculé", "tue", "hate", "kill", "hit", "punch",
        "imbécile", "Imbécile", "putain", "bordel", "merde", "nique", 
        "fils de pute", "clochard", "gouine", "tarlouze", "saloperie", 
        "conne", "couillon", "va te faire foutre", "pédé", "salope", 
        "vieux débris", "abruti", "bâtard", "casse-toi", "enfoiré", 
        "vas-y te faire foutre", "sale pute",
    ]
    
    for avis_item in avis:
        avis_item.stars = range(avis_item.rating)  # Filled stars
        avis_item.unfilled_stars = range(4 - avis_item.rating)  # Unfilled stars (assuming 5 stars max)
        avis_item.contains_bad_words = avis_item.check_bad_words(bad_words)  # Check for bad words
    
    return render(request, 'list.html', {'avis': avis})



@login_required
def avis_create(request):
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            avis = form.save(commit=False)
            avis.author = request.user   # Replace with test data or logic
                        # Get the selected ride from the form
            # Get the selected ride from the form
            # Get the selected ride from the form (this returns the full Ride object)
            ride = form.cleaned_data.get('ride')  

            # Assign the full Ride object to the recipient field, not just the ID
            avis.recipient = ride  # This is now the correct Ride object
            avis.save()
            return redirect('avis_list')
    else:
        form = AvisForm()  # Initialize the form here

    return render(request, 'Ajout.html', {'form': form})

@login_required
def avis_update(request, pk):
    avis = get_object_or_404(Avis, pk=pk)

    # Ensure the user is the author of the review
    if avis.author != request.user:
        return redirect('avis_list')  # Redirect if not the author

    if request.method == 'POST':
        form = AvisForm(request.POST, instance=avis)
        if form.is_valid():
            # Save the updated review
            updated_avis = form.save()

            # Set the 'approved' field to False to indicate it needs re-approval
            updated_avis.approved = False
            updated_avis.save()  # Save the review with the updated 'approved' field

            # Redirect to the review list page
            return redirect('avis_list')  # Redirect to avis_list after the update

    else:
        form = AvisForm(instance=avis)

    return render(request, 'Ajout.html', {'form': form})



def avis_delete(request, pk):
    avis = get_object_or_404(Avis, pk=pk)
    if request.method == 'POST':
        avis.delete()
        return redirect('avis_list')
    return render(request, 'delete.html', {'avis': avis})

def avis_approval(request):
    # Show only unapproved reviews
    bad_words = [
    "connard",
    "salaud",
    "enculé",
    "tue",
    "hate",
    "kill",
    "hit",
    "punch",
    "imbécile",
    "Imbécile",
    "putain",
    "bordel",
    "merde",
    "nique",
    "fils de pute",
    "clochard",
    "gouine",
    "tarlouze",
    "saloperie",
    "conne",
    "couillon",
    "va te faire foutre",
    "pédé",
    "salope",
    "vieux débris",
    "abruti",
    "bâtard",
    "casse-toi",
    "enfoiré",
    "vas-y te faire foutre",
    "sale pute",
]

    unapproved_avis = Avis.objects.filter(approved=False)
    return render(request, 'approve.html', {'avis': unapproved_avis, 'bad_words': bad_words})

def approve_avis(request, pk):
    bad_words = [
        "connard", "salaud", "enculé", "tue", "hate", "kill", "hit", "punch",
        "imbécile", "Imbécile", "putain", "bordel", "merde", "nique", 
        "fils de pute", "clochard", "gouine", "tarlouze", "saloperie", 
        "conne", "couillon", "va te faire foutre", "pédé", "salope", 
        "vieux débris", "abruti", "bâtard", "casse-toi", "enfoiré", 
        "vas-y te faire foutre", "sale pute",
    ]

    # Get the avis object
    avis = get_object_or_404(Avis, pk=pk)

    # Check if the comment contains bad words
    avis.contains_bad_words = avis.check_bad_words(bad_words)

    # Mark as approved
    avis.approved = True
    avis.save()

    return redirect('avis_approval')


def disapprove_avis(request, pk):
    avis = get_object_or_404(Avis, pk=pk)
    # Delete the Avis object
    avis.delete()
    # Redirect to the approval page (or wherever you need to redirect)
    return redirect('avis_approval')
