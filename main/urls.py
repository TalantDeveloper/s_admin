from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('types/', views.get_types, name='types'),
    path('types/<int:pk>/delete/', views.delete_type, name='delete_type'),
    path('computers/', views.get_computers, name='computers'),
    path('computers/create/', views.create_computer, name='create_computer'),
    path('computers/<int:pk>/delete/', views.delete_computer, name='delete_computer'),
    path('computers/<int:pk>/update/', views.update_computer, name="update_computer"),
    path('departments/', views.get_departments, name='departments'),
    path('departments/<int:pk>/delete/', views.delete_department, name='delete_department'),
    path('departments/<int:pk>/update/', views.update_department, name='update_department'),
    path('employees/', views.get_employees, name='employees'),
    path('employees/by_department/', views.get_employee_by_depart, name='by_department'),
    path('employees/by_type/', views.get_employee_by_type, name='by_type'),
    path('employees/ny_active/', views.get_employee_by_status, name='by_active'),

    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/create/cp/', views.create_employee_view, name='create-employee'),
    path('employees/<int:pk>/delete/', views.delete_employee, name='delete-employee'),
    path('employees/<int:pk>/update/', views.update_employee, name='update-employee'),
    path('employees/<int:pk>/update/easy/', views.update_employee_easy, name='update-employee-easy'),
    path('employees/<int:pk>/update/full/', views.update_employee_full, name='update-employee-full'),


    path('full/', views.report_full, name='report_full'),

]
