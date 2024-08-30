from django.shortcuts import render
from .models import Type, Computer, Department, Employee


def get_types(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        pc_type = Type.objects.create(name=name, image=image)
        pc_type.save()

    types = Type.objects.all()
    context = {'types': types}
    return render(request, 'main/type.html', context)


def get_computers(request):
    computers = Computer.objects.all()
    types = Type.objects.all()
    context = {'computers': computers, 'types': types}
    return render(request, 'main/computer.html', context)


def get_departments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = Department.objects.create(name=name)
        department.save()

    departments = Department.objects.all()
    types = Type.objects.all()
    context = {'departments': departments, 'types': types}
    return render(request, 'main/departments.html', context)


def get_employees(request):
    employees = Employee.objects.all()
    types = Type.objects.all()
    computers = Computer.objects.all()
    departments = Department.objects.all()
    context = {'employees': employees, 'types': types, 'computers': computers,
               'departments': departments}
    return render(request, 'main/employees.html', context)