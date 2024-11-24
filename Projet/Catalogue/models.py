from django.db import models
from django.core.validators import MaxValueValidator, FileExtensionValidator, ValidationError
from datetime import date

def validate_future_date(start_date):
    if start_date <= date.today():
        raise ValidationError('Cette date doit être une date future ')


class Offre(models.Model):
    title = models.CharField(("Title"), max_length=150, unique=True)
    description = models.TextField(("description"))
    start_date = models.DateField(("start date"), validators=[validate_future_date])
    end_date = models.DateField(("end date"))
    price = models.IntegerField(("prix"))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="all_conferences")
    
    def __str__(self) -> str:
        return self.title
    
    def clean(self) -> None:
        
        if self.end_date <= self.start_date:
            raise ValidationError({
                'end_date': "End date must be set after start date."})