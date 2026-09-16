from django import forms

class PlaylistForm(forms.Form):
    title = forms.CharField(label='Название плейлиста', max_length=100)
    genre = forms.CharField(label='Жанр', max_length=50)
    description = forms.CharField(label='Описание', widget=forms.Textarea, required=False)