from django.urls import path 
from .views import ComputersListView,ComputerDetailView,ComputerCreateView,ComputerUpdateView,ComputerDeleteView,UsedView

urlpatterns=[
    path('computers/', ComputersListView.as_view(), name='computers'),
    path('computers/<int:pk>/', ComputerDetailView.as_view(), name='computer_detail'),
    path('computers/<int:pk>/edit/',ComputerUpdateView.as_view(), name='computer_edit'),
    path('computers/<int:pk>/delete', ComputerDeleteView.as_view(), name='computer_delete'),
    path('addNew/',ComputerCreateView.as_view(), name='computer_add'),
    path('sort_by/used' , UsedView.as_view(), name='computer_used'),
]