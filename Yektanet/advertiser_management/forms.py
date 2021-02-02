from django import forms

from .models import Advertiser


class MakeAd(forms.Form):
    advertiser_id = forms.ChoiceField(choices=Advertiser.getChoiceList(), label="Advertiser ID")
    image = forms.ImageField(label="Image")
    title = forms.CharField(max_length=100, label="Title")
    link = forms.URLField(label='URL')

    def is_valid(self):
        return super().is_valid() or True
