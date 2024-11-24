from django.shortcuts import render, get_object_or_404, redirect
from .models import Avis
from .forms import AvisForm
from userapp.models import user

def avis_list(request):
    # Check if the filter parameter exists in the request
    sort_by_rating = request.GET.get('sort_by', None)
    
    if sort_by_rating == 'rating_desc':
        avis = Avis.objects.filter(approved=True).order_by('-rating')  # Most rated first
    else:
        avis = Avis.objects.filter(approved=True)  # Default order
    
    return render(request, 'list.html', {'avis': avis})

def avis_create(request):
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            avis = form.save(commit=False)
            # Assign the author and recipient programmatically
            avis.author = user.objects.get(username="john_doe")  # Replace with test data or logic
            avis.recipient = user.objects.get(username="jane_smith")  # Replace with test data or logic
            avis.save()
            return redirect('avis_list')
    else:
        form = AvisForm()
    return render(request, 'Ajout.html', {'form': form})

def avis_update(request, pk):
    avis = get_object_or_404(Avis, pk=pk)
    if request.method == 'POST':
        form = AvisForm(request.POST, instance=avis)
        if form.is_valid():
            form.save()
            return redirect('avis_list')
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
    # Get the avis object
    avis = get_object_or_404(Avis, pk=pk)
    # Set the 'approved' field to True
    avis.approved = True
    avis.save()
    return redirect('avis_approval')  

def disapprove_avis(request, pk):
    avis = get_object_or_404(Avis, pk=pk)
    # Delete the Avis object
    avis.delete()
    # Redirect to the approval page (or wherever you need to redirect)
    return redirect('avis_approval')
