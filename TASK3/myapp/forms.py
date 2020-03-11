from django import forms

from .models import Snippet


# creating fields in the form using forms.Form
class ContactForms(forms.Form):
    name = forms.CharField()
    Phone = forms.IntegerField()
    Email = forms.EmailField(label='E-mail')


#creating fields in the form using using forms.ModelForm to use in admin panel

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'Phone', 'Email')
