from django import forms
from survey.models import Reasons, Influences

class ReasonsForm(forms.ModelForm):


    class Meta:
        
        model = Reasons
        fields = ['position', 'influences', 'additional_description']
        widgets = {
            'influences': forms.CheckboxSelectMultiple(),
        }