# avis/models.py
from django.db import models
from userapp.models import user
from Rides.models import Ride  # Import the Ride model


class Avis(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 5)] 
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Add this field for approval
    contains_bad_words = models.BooleanField(default=False)  # Add this field to store bad words check

    author = models.ForeignKey(user, related_name='given_reviews', on_delete=models.CASCADE)  # Reviewer
    recipient = models.ForeignKey(Ride, related_name='received_reviews', on_delete=models.CASCADE)  # Link to the Ride model (reviewed ride)
    ride = models.ForeignKey(Ride, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)  # Link to Ride

    def __str__(self):
        return f'{self.rating} Etoiles by {self.author} for {self.recipient}'

    def check_bad_words(self, bad_words):
        """
        Checks if the comment contains any bad words.
        """
        for word in bad_words:
            if word.lower() in self.comment.lower():
                return True
        return False
