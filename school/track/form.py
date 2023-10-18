from django import forms


class AddTrackForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Track Name",
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Enter track name',
                                      'class': 'form-control'}
                               )
                           )
