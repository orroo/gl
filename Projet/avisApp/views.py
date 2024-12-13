from django.shortcuts import render, get_object_or_404, redirect
from .models import Avis
from .forms import AvisForm
from userapp.models import user
from Rides.models import Ride
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import google.generativeai as genai
from django.conf import settings
import time



genai.configure(api_key="AIzaSyBmVi62z-xYpSov5XZhjvH5DVc07d2UdKA")
model = genai.GenerativeModel("gemini-1.5-flash")

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

import google.generativeai as genai
from django.shortcuts import render, get_object_or_404, redirect
from .models import Avis
from .forms import AvisForm




def check_for_violence(text):
    try:
        # Generate content and analyze sentiment and violence
        response = model.generate_content(f"Analyze the following text for violent language and emotion in one sentence: {text}")
        analysis = response.text
        
        # You can enhance this logic by parsing the response to extract specific emotions or violence indicators
        return analysis
    except Exception as e:
        print(f"Error in generating AI response: {e}")
        return "Error analyzing content"
    
def check_for_emotion(text):
    try:
        # Generate content and analyze sentiment and violence
        response = model.generate_content(f"Analyze the following text to classify the emotion in two or three words you need to include 'satisfied: your analysis in two or three words' or 'unsatisfied: your analysis in two or three words': {text}")
        emotion = response.text
        
        # You can enhance this logic by parsing the response to extract specific emotions or violence indicators
        return emotion
    except Exception as e:
        print(f"Error in generating AI response: {e}")
        return "Error analyzing content"


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

    # Analyzing reviews for violent behavior and emotion detection
    reviews_with_analysis = []

    for avis_item in unapproved_avis:
        # Get the content of the review
        review_text = avis_item.comment
        
        # Run the analysis on the review text
        analysis = check_for_violence(review_text)
        emotions=check_for_emotion(review_text)
        # Store the result (the review and its analysis)
        reviews_with_analysis.append({
            'avis': avis_item,
            'analysis': analysis,
            'emotions': emotions
        })

    return render(request, 'approve.html', {'reviews_with_analysis': reviews_with_analysis ,'avis': unapproved_avis, 'bad_words': bad_words})



def calculate_satisfaction_percentage(request):
    # Get all approved reviews
    approved_avis = Avis.objects.filter(approved=False)

    # Initialize counters
    satisfied_count = 0
    non_satisfied_count = 0

    # Analyze each review
    for avis_item in approved_avis:
        review_text = avis_item.comment
        emotion = check_for_emotion(review_text)
        emotion_first_11_lower = emotion[:11].lower()
        emotion_first_10_lower = emotion[:9].lower()
        if 'satisfied' in emotion_first_10_lower:
            satisfied_count += 1
        elif 'unsatisfied' in emotion_first_11_lower:
            non_satisfied_count += 1

    # Calculate percentages
    total_reviews = satisfied_count + non_satisfied_count
    satisfied_percentage = (satisfied_count / total_reviews) * 100 if total_reviews > 0 else 0
    non_satisfied_percentage = (non_satisfied_count / total_reviews) * 100 if total_reviews > 0 else 0

    context = {
        'total_reviews': total_reviews,
        'satisfied_count': satisfied_count,
        'non_satisfied_count': non_satisfied_count,
        'satisfied_percentage': satisfied_percentage,
        'non_satisfied_percentage': non_satisfied_percentage
    }

    return render(request, 'avisStat.html', context)



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
