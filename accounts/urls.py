from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('generate_user_token', obtain_auth_token),
    path('get_my_details', MyDetailsView.as_view()),
    path('signup',SignUpView.as_view()),
]