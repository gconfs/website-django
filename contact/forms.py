from django import forms
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' :
        'form-control'}), max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class' :
        'form-control'}), max_length=100)
    cc_myself = forms.BooleanField(required=False)
    captcha = ReCaptchaField()
