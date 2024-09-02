from django.shortcuts import render, redirect, get_object_or_404
from .models import Type, Computer, Department, Employee
from .function import department_get, computer_get, computer_update


def welcome(request):
    return render(request, 'main/welcome.html')


def get_types(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        pc_type = Type.objects.create(name=name, image=image)
        pc_type.save()
        return redirect('main:types')

    types = Type.objects.all()
    context = {'types': types}
    return render(request, 'main/type.html', context)


def delete_type(request, pk):
    pc_type = Type.objects.get(pk=pk)
    pc_type.delete()
    return redirect('main:types')


def get_computers(request):
    computers = Computer.objects.all()
    types = Type.objects.all()
    context = {'computers': computers, 'types': types}
    return render(request, 'main/computer.html', context)


def create_computer(request):
    if request.method == 'POST':
        invention_id = request.POST.get('invention_id')
        years = request.POST.get('years')
        pc_type = Type.objects.get(pk=int(request.POST.get('type')))
        is_active = True if request.POST.get('is_active') == 'True' else False
        computer = Computer.objects.create(invention_id=invention_id, years=years, type=pc_type, is_active=is_active)
        computer.save()
        return redirect('main:computers')


def update_computer(request, pk):
    if request.method == "POST":
        computer = computer_update(request, pk)
        return redirect('main:computers')
    computer = Computer.objects.get(pk=pk)
    types = Type.objects.all()
    computers = Computer.objects.all()
    context = {
        'computer': computer,
        'types': types,
        'computers': computers
    }
    return render(request, 'main/update_computer.html', context)


def delete_computer(request, pk):
    computer = Computer.objects.get(pk=pk)
    computer.delete()
    return redirect('main:computers')


def get_departments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = Department.objects.create(name=name)
        department.save()
        return redirect('main:departments')

    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'main/departments.html', context)


def delete_department(request, pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect('main:departments')


def update_department(request, pk):
    if request.method == "POST":
        name = request.POST.get('name')
        department = Department.objects.get(pk=pk)
        department.name = name
        department.save()
        return redirect("main:departments")
    department = Department.objects.get(pk=pk)
    departments = Department.objects.all()
    context = {
        'department': department,
        'departments': departments
    }
    return render(request, 'main/update_department.html', context)


def get_employees(request):
    employees = Employee.objects.all()
    types = Type.objects.all()
    computers = Computer.objects.all()
    departments = Department.objects.all()
    context = {'employees': employees, 'types': types, 'computers': computers,
               'departments': departments}
    return render(request, 'main/employees.html', context)


def get_employee_by_depart(request):
    types = Type.objects.all()
    departments = Department.objects.all()
    if request.method == "POST":
        department_id = int(request.POST.get('department'))
        employees = Employee.objects.filter(department=department_id)
        context = {
            'types': types,
            'departments': departments,
            'employees': employees
        }

        return render(request, 'main/employees.html', context)


def get_employee_by_type(request):
    types = Type.objects.all()
    departments = Department.objects.all()
    if request.method == "POST":
        pc_type = int(request.POST.get('type'))
        employees = Employee.objects.filter(computer__type=pc_type)
        context = {
            'types': types,
            'departments': departments,
            'employees': employees
        }
        return render(request, 'main/employees.html', context)


def get_employee_by_status(request):
    if request.method == 'POST':
        is_active = True if request.POST.get('is_active') == 'True' else False
        employees = Employee.objects.filter(computer__is_active=is_active)
    else:
        employees = Employee.objects.all()
    types = Type.objects.all()
    departments = Department.objects.all()
    context = {
        'types': types,
        'departments': departments,
        'employees': employees
    }
    return render(request, 'main/employees.html', context)


def create_employee(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        department = department_get(request)
        computer = computer_get(request)
        employee = Employee.objects.create(full_name=full_name, department=department, computer=computer)
        employee.save()
        return redirect('main:create_employee')
    types = Type.objects.all()
    departments = Department.objects.all()
    computers = Computer.objects.all()

    context = {
        'types': types,
        'departments': departments,
        'computers': computers
    }

    return render(request, 'main/create_employee.html', context)


def create_employee_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        department = department_get(request)
        invention_id = request.POST.get('invention_id')
        pc_type = Type.objects.get(pk=int(request.POST.get('type')))
        is_active = True if request.POST.get('is_active') == 'True' else False
        years = request.POST.get('years')
        computer = Computer.objects.create(invention_id=invention_id, type=pc_type, is_active=is_active, years=years)
        computer.save()
        employee = Employee.objects.create(full_name=full_name, department=department, computer=computer)
        return redirect('main:create_employee')
    types = Type.objects.all()
    departments = Department.objects.all()
    computers = Computer.objects.all()
    context = {
        'types': types,
        'departments': departments,
        'computers': computers
    }
    return render(request, 'main/create_employee.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('main:employees')


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    types = Type.objects.all()
    departments = Department.objects.all()
    computers = Computer.objects.all()
    context = {
        'employee': employee,
        'types': types,
        'departments': departments,
        'computers': computers

    }
    return render(request, 'main/update_employees.html', context)


def update_employee_easy(request, pk):
    if request.method == "POST":
        employee = Employee.objects.get(pk=pk)
        department = department_get(request)
        computer = computer_get(request)
        employee.full_name = request.POST.get('full_name')
        employee.department = department
        employee.computer = computer
        employee.save()
        return redirect('main:employees')


def update_employee_full(request, pk):
    if request.method == "POST":
        employee = Employee.objects.get(pk=pk)
        employee.full_name = request.POST.get('full_name')
        employee.department = department_get(request)
        employee.computer = computer_update(request, employee.computer.id)
        employee.save()
        return redirect('main:employees')


def report_full(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'xisobot/full.html', context)

