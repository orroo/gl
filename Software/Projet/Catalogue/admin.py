from django.contrib import admin
from .models import Offre
from django.utils import timezone

class OffreAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'price') #now details show as table columns when i consult all conferences
    ordering = ('title', 'start_date') # there will be ordering option by title and start_date
    list_per_page = 1
    readonly_fields = ('created_at', 'updated_at') # can't modify these fields anymore
    list_filter = ('title',) #adds a filter option 
    search_fields = ('title',) #adds a search bar that works by title, by location #this adds the inline that was defined above
    fieldsets = (
        (
            'Description',
            {
                'fields': ('title', 'description')
            }
         ),
        (
            'Période',
            {
                'fields': ('start_date', 'end_date')
            }
        ),
        (
            'Informations de la conférence',
            {
                'fields': ( 'price', )
            }
        ),
        (
            'Timestamps',
            {
                'fields': ('created_at', 'updated_at')
            }
        )
        
    )
# Register your models here.
admin.site.register(Offre, OffreAdmin)