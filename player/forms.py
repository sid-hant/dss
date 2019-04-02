from django import forms
from .models import Player

class searchPlayer(forms.ModelForm):
    
    value=forms.FloatField(required=False)
    pace=forms.IntegerField(required=False)
    shooting=forms.IntegerField(required=False)
    passing=forms.IntegerField(required=False)
    dribbling=forms.IntegerField(required=False)
    defence=forms.IntegerField(required=False)
    physical=forms.IntegerField(required=False)


    class Meta():
        model = Player
        fields = ('value', 'pace', 'shooting', 'passing', 'dribbling',  'defence', 'physical',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class searchGK(forms.ModelForm):
    
    value=forms.FloatField(required=False)
    pace=forms.IntegerField(required=False, label="Diving")
    shooting=forms.IntegerField(required=False, label="Handling")
    passing=forms.IntegerField(required=False, label="Kicking")
    dribbling=forms.IntegerField(required=False, label="Reflexes")
    defence=forms.IntegerField(required=False, label="Speed")
    physical=forms.IntegerField(required=False, label="Position")


    class Meta():
        model = Player
        fields = ('value', 'pace', 'shooting', 'passing', 'dribbling',  'defence', 'physical',)
        labels = {'pace':'Diving', 'shooting':'Handling', 'passing':'Kicking', 'dribbling':'Reflexes','defence':'Speed','physical':'Position'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




