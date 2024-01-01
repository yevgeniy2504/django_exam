from django import forms
from ..models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'photo', 'bio']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Enter author name'})}
