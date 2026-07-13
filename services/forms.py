from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    area = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)