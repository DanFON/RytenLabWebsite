from django import forms

class contactForm(forms.Form):
    # name= forms.CharField(required=True, max_length=100, help_text='100 characters max.')
    name= forms.CharField(required=True, max_length=100, help_text='')
    email=forms.EmailField(required=True)
    message=forms.CharField(required=True, widget=forms.Textarea)