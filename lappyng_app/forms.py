from django import forms
from lappyng_app.models import *



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }