from django.urls import path
from .views import *

urlpatterns = [
    path('patients/', RetrievePatientListView.as_view())
]