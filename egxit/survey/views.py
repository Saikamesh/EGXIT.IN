from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from survey.forms import ReasonsForm

# Create your views here.
def index(request):
    return render(request, "survey/index.html")

class ReasonsWizardView(SessionWizardView):
    form_list = [ReasonsForm]
    template_name = 'survey/reasons_form.html'

    def done(self, form_list, **kwargs):
        return HttpResponse("Thank you for your submission.")
