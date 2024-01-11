from django import forms
from survey.models import Reasons, Influences, WorkLifeMetrics, OtherPosition, OverallWorkExperience, PersonalDetails


class ReasonsForm(forms.ModelForm):
    
    INFLUENCES_CHOICES = {
        'A': 'Choice A',
        'B': 'Choice B',
        'C': 'Choice C',
        'D': 'Choice D',
        'E': 'Choice E',
        'F': 'Choice F',
        'G': 'Choice G',
        'H': 'Choice H',
        'I': 'Choice I',
        'J': 'Choice J'
    }
    influences = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=INFLUENCES_CHOICES)

    class Meta:
        model = Reasons
        fields = '__all__'
        widgets = {
            'position': forms.RadioSelect(attrs={'class': 'custom-radio'}),
        }
        

    def __init__(self, *args, **kwargs):
        super(ReasonsForm, self).__init__(*args, **kwargs)
        self.fields['position'].choices = [choice for choice in self.fields['position'].choices if choice[0] != '']


class OtherPositionForm(forms.ModelForm):
    class Meta:
        model = OtherPosition
        fields = '__all__'


class WorkLifeMetricsForm(forms.ModelForm):
    class Meta:
        model = WorkLifeMetrics
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(WorkLifeMetricsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget = forms.RadioSelect()
            if isinstance(field, forms.ChoiceField):
                field.choices = [choice for choice in field.choices if choice[0] != '']
                

class OverallWorkExperienceForm(forms.ModelForm):
    class Meta:
        model = OverallWorkExperience
        fields = '__all__'


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__' 
        