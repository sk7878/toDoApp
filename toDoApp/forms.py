from django import forms
from .models import ToDoModel


class ToDoModelForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title',
                'class': 'form-control'
            }
        )
    )
    detail = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Additional detail',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = ToDoModel
        fields = ['title', 'detail']
