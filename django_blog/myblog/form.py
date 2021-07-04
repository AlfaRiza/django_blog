from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'row': 3,
        'placeholder': 'Join the discussion and leave a comment!',
        'id': 'usercomment',
    }))

    class Meta:
        model = Comment
        fields = ('content', )


