from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userauth.models import Userauth

class CustomUserAdmin(UserAdmin):
    model = Userauth
    list_display = ('username', 'email', 'first_name', 'last_name')  # Affichage des champs pertinents
    list_filter = ('is_active', 'is_staff')  # Liste des filtres disponibles
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Gestion du mot de passe
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'birth_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')  # Recherche par 'username' ou 'email'
    ordering = ('email',)

admin.site.register(Userauth, CustomUserAdmin)

