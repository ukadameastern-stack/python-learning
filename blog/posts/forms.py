from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_content"]

        widgets = {
            "comment_content": forms.Textarea(attrs={
                "placeholder": "Write your comment...",
                "rows": 4,
                "class": "form-textarea"
            }),
        }