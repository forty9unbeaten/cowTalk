from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='What does the cow say?', max_length=150)
