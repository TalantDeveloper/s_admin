from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import Type, Computer, Department, Employee


def login_function(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main:welcome')
    else:
        return redirect('main:login')


def department_get(request):
    try:
        department_id = int(request.POST.get('department'))
        department = Department.objects.get(pk=department_id)
    except ValueError:
        department = None
    return department


def computer_get(request):
    try:
        computer_id = int(request.POST.get('computer'))
        computer = Computer.objects.get(pk=computer_id)
    except ValueError:
        computer = None
    return computer


def computer_update(request, pk):
    invention_id = request.POST.get('invention_id')
    pc_type = Type.objects.get(pk=int(request.POST.get('type')))
    is_active = True if request.POST.get('is_active') == 'True' else False
    computer = Computer.objects.get(pk=pk)
    computer.invention_id = invention_id
    computer.type = pc_type
    computer.is_active = is_active
    computer.save()
    return computer


def content_get(request):
    types = Type.objects.all()
    departments = Department.objects.all()
    computers = Computer.objects.all()
    employees = Employee.objects.all()
    context = {
        'types': types,
        'types_length': len(types),
        'departments': departments,
        'departments_length': len(departments),
        'computers': computers,
        'computers_length': len(computers),
        'employees': employees,
        'employees_length': len(employees),

    }
    return context
