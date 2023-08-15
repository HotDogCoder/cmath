from django.urls import path
from .views import *


urlpatterns = [
    path('screenshot', StartMonitoreo.as_view()),
    path('report-type', ReportTypeView.as_view()),
    path('image-processor', ImageProcessorView.as_view()),
    path('test-cmath', CmathView.as_view()),
    path('run-speech', SpeechView.as_view()),
    # path('profile/<account>', DetailUserProfileView.as_view()),
]