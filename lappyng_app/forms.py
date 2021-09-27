from django import forms
from lappyng_app.models import *
from django.core import validators



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class ProductReviewForm(forms.ModelForm):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    CHOOSE = ''
    RATING_LIST = [
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
        (CHOOSE, 'Choose Rating'),
    ]

    full_name = forms.CharField(
                widget = forms.TextInput(
                    attrs={'class':'form-control', 'placeholder':'Fullname'}
                ),
                )
    email = forms.EmailField(
                widget = forms.EmailInput(
                    attrs={'class':'form-control', 'placeholder':'Email'}
                ),
                )
    rating = forms.CharField(
                widget = forms.Select(
                    attrs={'class':'form-control',},
                    choices=RATING_LIST,
                ),
                )
    review = forms.CharField(
                widget = forms.Textarea(
                    attrs={'class':'form-control',}
                ),
                )
    botcatcher = forms.CharField(
        required=False, 
        widget=forms.HiddenInput, 
        validators=[validators.MaxLengthValidator(0)])

    
    class Meta:
        model = ProductReview
        exclude = ('created_at', 'updated', 'product')


class ProductRequestForm(forms.ModelForm):
    name = forms.CharField(
                widget = forms.TextInput(
                    attrs={'class':'form-control', 'placeholder':'Fullname'}
                ),
                )
    email = forms.EmailField(
                widget = forms.EmailInput(
                    attrs={'class':'form-control', 'placeholder':'Email'}
                ),
                )
    phone = forms.CharField(
                widget = forms.TextInput(
                    attrs={'class':'form-control', 'placeholder':'Phone'}
                ),
                )
    description = forms.CharField(
                widget = forms.Textarea(
                    attrs={'class':'form-control',}
                ),
                )
    botcatcher = forms.CharField(
        required=False, 
        widget=forms.HiddenInput, 
        validators=[validators.MaxLengthValidator(0)])

    
    class Meta:
        model = ProductRequest
        exclude = ('created', 'modified', 'product')

        