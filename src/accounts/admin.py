from django.contrib import admin

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ['-id']
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    readonly_fields = ('password', 'email', 'join_date', 'last_login')
    exclude = ('password',)
