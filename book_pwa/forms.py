from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["user"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write a comment",
                }
            ),
            "rating": forms.Select(attrs={"class": "form-select"}),
        }
