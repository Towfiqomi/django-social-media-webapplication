from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Update your status.....',
        }
    ))

    class Meta:
        model = Post
        fields = ('content',)
