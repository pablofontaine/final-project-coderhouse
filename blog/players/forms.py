from django import forms

from players.models import TennisPlayer


class TennisPlayerForm(forms.ModelForm):

    class Meta:
        model = TennisPlayer
        fields = ['name', 'country', 'retired']
#        widgets = {
#            'name': forms.TextInput(attrs={'placeholder': ''}),
#            'country' : forms.TextInput(attrs={'placeholder': ''}),
#        }
