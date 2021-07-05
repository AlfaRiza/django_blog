from django import forms
from .models import *
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use__required__attribute(self, *args):
        return False


# class AddCategoryForm(forms.ModelForm):
#     content = forms.CharField(
#     )
#
#     class Meta:
#         model = Category
#         fields = ['title', 'content']


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs= {'required': False, 'cols': 30, 'rows': 10,}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'description', 'content', 'thumbnail', 'categories', 'featured')


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


