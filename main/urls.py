from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('types/', views.get_types, name='types'),
    path('types/<int:id>/delete/', views.delete_type, name='delete_type'),
    path('computers/', views.get_computers, name='computers'),
    path('departments/', views.get_departments, name='departments'),
    path('departments/<int:pk>/delete/', views.delete_department, name='delete_department'),
    path('employees/', views.get_employees, name='employees'),
    
]
