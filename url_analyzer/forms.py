from django import forms
from .models import UrlSentimentModel


class UrlSentimentForm(forms.ModelForm):
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={'class': 'form-control form-control-lg d-inline',
                   'placeholder': 'Your URLs to Test Sentiment'
                   }
        ))

    class Meta:
        model = UrlSentimentModel
        fields = ['url']

    # def save(self):
