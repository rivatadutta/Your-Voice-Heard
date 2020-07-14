from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_name', 'issue_text']
        widgets = {
            'issue_name': forms.TextInput(
            attrs={'id': 'issname', 'class':'input', 'placeholder': 'Name of your issue', 'aria-label' : 'Issue Title'}),
            
            'issue_text': forms.Textarea(
            attrs={'id': 'isstxt', 'class':'input', 'placeholder': 'Enter a relavent political issue we should put resources for on the site.', 'aria-label' : 'Issue Text'})
        }
    