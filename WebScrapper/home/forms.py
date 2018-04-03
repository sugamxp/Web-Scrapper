from django import forms

class FormName(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Type Here.'}),label='')
