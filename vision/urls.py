from django.urls import path
from .views import *
app_name = 'vision'
urlpatterns = [
    path('detect_dr',detect_dr, name="detect_dr"),
    path('detect_dr_result',detect_dr_result, name="detect_dr_result"),
]