from django import forms
from track.models import *


class AddTraineeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Trainee Name",
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Enter trainee name',
                                      'class': 'form-control'}
                               )
                           )

    birthdate = forms.DateField(required=True,
                                widget=forms.DateInput(
                                    attrs={'type': 'date',
                                           'class': 'form-control'}
                                    )
                                )

    track = forms.ChoiceField(required=True, choices=[(track.id, track.name) for track in Track.objects.all()],
                              widget=forms.Select(
                                  attrs={'class': 'form-control'})
                              )
