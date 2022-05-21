from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from src.accounts.models import Profile


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('email', 'password')


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        exclude = ('email', 'password', 'join_date', 'last_login')
