from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from survey.forms import ReasonsForm, OtherPositionForm, WorkLifeMetricsForm, OverallWorkExperienceForm, PersonalDetailsForm


def index(request):
    return render(request, "survey/index.html")


def show_personaldetailsform(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('3') or {}
    return cleaned_data.get('in_person_interview')


def show_otherpositionform(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    return cleaned_data.get('position') == 'OT'


class ReasonsWizardView(SessionWizardView):
    form_list = [ReasonsForm, OtherPositionForm, WorkLifeMetricsForm, OverallWorkExperienceForm, PersonalDetailsForm]
    template_name = 'survey/reasons_form.html'

    condition_dict = {
        '1': show_otherpositionform,
        '4': show_personaldetailsform
        }
    

    def done(self, form_list, **kwargs):
        print(form_list[0].cleaned_data)
        print(form_list[1].cleaned_data)
        print(form_list[2].cleaned_data)
        print(form_list[3].cleaned_data)
        print(form_list[4].cleaned_data)
        return HttpResponse("Thank you for your submission.")
