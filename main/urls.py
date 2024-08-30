from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('types/', views.get_types, name='types'),
    path('computers/', views.get_computers, name='computers'),
    path('departments/', views.get_departments, name='departments'),
    path('employees/', views.get_employees, name='employees'),
    
]
