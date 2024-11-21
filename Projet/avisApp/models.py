from django.db import models
from userapp.models import user
class Avis(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 5)] 
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Add this field for approval

    author = models.ForeignKey(user, related_name='given_reviews', on_delete=models.CASCADE)  # Reviewer
    recipient = models.ForeignKey(user, related_name='received_reviews', on_delete=models.CASCADE)  # Reviewee

    def __str__(self):
        return f'{self.rating} Etoiles by {self.author} for {self.recipient}'
 