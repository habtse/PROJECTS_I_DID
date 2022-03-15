from django.urls import path
from .views import ComputerSignUpView

urlpatterns=[
    path('signup/', ComputerSignUpView.as_view(),name='signup'),
]