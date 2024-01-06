from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reasons/", views.ReasonsWizardView.as_view(), name="reasons")
]