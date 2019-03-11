from django import forms
from .models import CreateDiscussion

class DiscussionForm(forms.ModelForm):
    discussion_title=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Discussion Title.....',
        }
    ))

    class Meta:
        model = CreateDiscussion
        fields = ('discussion_title',)
