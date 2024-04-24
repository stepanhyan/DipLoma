from compositions.models import Songs
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput
from django import forms


class LikeForm(forms.Form):
    song_id = forms.IntegerField()
    print("SongID", song_id)


class CommentForm(forms.Form):
    song_id = forms.IntegerField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment_input'}))
    print("SongID from forms", song_id)
    print("Comment from Forms", comment)


class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['title', 'image', 'audio']
        labels = {
            'title': '',
            'image': '',
            'audio': '',
        }

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Product's name"
            }),
            "image": FileInput(attrs={
                'class': 'form-control'
            }),
            "audio": FileInput(attrs={
                'class': 'form-control',
            })
        }
