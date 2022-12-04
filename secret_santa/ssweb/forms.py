

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

class JoinGameForm(forms.Form):
    name = forms.CharField(help_text='Enter your name')
    secret_word = forms.CharField(help_text='Enter a secret word that you will remember')
    wishlist = forms.CharField(widget=forms.Textarea, help_text='Enter what you want for Christmas')

class ReviewLoginForm(forms.Form):
    name = forms.CharField(help_text='Enter your name')
    secret_word = forms.CharField(help_text='Enter the secret word you picked earlier')

class EditWishlistForm(forms.Form):
    wishlist = forms.CharField(widget=forms.Textarea, help_text='Update your wishlist')