from django.contrib.auth import forms, get_user_model

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    
    class Meta(forms.UserCreationForm.Meta):
        model = User
