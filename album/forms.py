from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta: 
        model = Album
        fields = '__all__'
        # fields = ['name', 'bio']
        # exclude = ['bio']