from django.urls import path
from obstetric.views import *

urlpatterns = [
    path('form/create/', ObstetricFomCreateView.as_view()),
    path('form/update/', ObstetricFormUpdateView.as_view()),
    path('physicalexam/update/', PhysicalExamUpdateView.as_view()),
    path('list/', ObstetricListView.as_view()),
    path('read/', ObstetricReadView.as_view()),
    path('delete/', ObstetricDeleteView.as_view()),
    path('physical/delete/', DeletePhysicalExam.as_view()),

]
