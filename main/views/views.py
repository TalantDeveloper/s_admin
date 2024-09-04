from django.shortcuts import render, redirect
from main.models import Type, Computer, Department, Employee
from main.function import department_get, computer_get, computer_update, content_get
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
def welcome(request):
    context = content_get(request)
    return render(request, 'main/welcome.html', context)


@login_required(login_url='main:login')
def get_types(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        pc_type = Type.objects.create(name=name, image=image)
        pc_type.save()
        return redirect('main:types')

    context = content_get(request)
    return render(request, 'main/type.html', context)


@login_required(login_url='main:login')
def delete_type(request, pk):
    pc_type = Type.objects.get(pk=pk)
    pc_type.delete()
    return redirect('main:types')


@login_required(login_url='main:login')
def get_computers(request):
    context = content_get(request)
    return render(request, 'main/computer.html', context)


@login_required(login_url='main:login')
def create_computer(request):
    if request.method == 'POST':
        invention_id = request.POST.get('invention_id')
        years = request.POST.get('years')
        pc_type = Type.objects.get(pk=int(request.POST.get('type')))
        is_active = True if request.POST.get('is_active') == 'True' else False
        computer = Computer.objects.create(invention_id=invention_id, years=years, type=pc_type, is_active=is_active)
        computer.save()
        return redirect('main:computers')


@login_required(login_url='main:login')
def update_computer(request, pk):
    if request.method == "POST":
        computer = computer_update(request, pk)
        return redirect('main:computers')
    computer = Computer.objects.get(pk=pk)
    context = content_get(request)
    context['computer'] = computer
    return render(request, 'main/update_computer.html', context)


@login_required(login_url='main:login')
def delete_computer(request, pk):
    computer = Computer.objects.get(pk=pk)
    computer.delete()
    return redirect('main:computers')


@login_required(login_url='main:login')
def get_departments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = Department.objects.create(name=name)
        department.save()
        return redirect('main:departments')

    context = content_get(request)
    return render(request, 'main/departments.html', context)


@login_required(login_url='main:login')
def delete_department(request, pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect('main:departments')


@login_required(login_url='main:login')
def update_department(request, pk):
    if request.method == "POST":
        name = request.POST.get('name')
        department = Department.objects.get(pk=pk)
        department.name = name
        department.save()
        return redirect("main:departments")
    department = Department.objects.get(pk=pk)
    context = content_get(request)
    context['department'] = department
    return render(request, 'main/update_department.html', context)


@login_required(login_url='main:login')
def get_employees(request):
    context = content_get(request)
    return render(request, 'main/employees.html', context)


@login_required(login_url='main:login')
def get_employee_by_depart(request):
    types = Type.objects.all()
    departments = Department.objects.all()
    if request.method == "POST":
        department_id = int(request.POST.get('department'))
        employees = Employee.objects.filter(department=department_id)
        context = {
            'types': types,
            'departments': departments,
            'employees': employees,
            'computers': Computer.objects.all()
        }

        return render(request, 'main/employees.html', context)


@login_required(login_url='main:login')
def get_employee_by_type(request):
    types = Type.objects.all()
    departments = Department.objects.all()
    if request.method == "POST":
        pc_type = int(request.POST.get('type'))
        employees = Employee.objects.filter(computer__type=pc_type)
        context = {
            'types': types,
            'departments': departments,
            'employees': employees,
            'computers': Computer.objects.all()
        }
        return render(request, 'main/employees.html', context)


@login_required(login_url='main:login')
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
        'employees': employees,
        'computers': Computer.objects.all()
    }
    return render(request, 'main/employees.html', context)


@login_required(login_url='main:login')
def create_employee(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        department = department_get(request)
        computer = computer_get(request)
        employee = Employee.objects.create(full_name=full_name, department=department, computer=computer)
        employee.save()
        return redirect('main:create_employee')
    context = content_get(request)
    return render(request, 'main/create_employee.html', context)


@login_required(login_url='main:login')
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
    context = content_get(request)
    return render(request, 'main/create_employee.html', context)


@login_required(login_url='main:login')
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('main:employees')


@login_required(login_url='main:login')
def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    context = content_get(request)
    context['employee'] = employee
    return render(request, 'main/update_employees.html', context)


@login_required(login_url='main:login')
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


@login_required(login_url='main:login')
def update_employee_full(request, pk):
    if request.method == "POST":
        employee = Employee.objects.get(pk=pk)
        employee.full_name = request.POST.get('full_name')
        employee.department = department_get(request)
        employee.computer = computer_update(request, employee.computer.id)
        employee.save()
        return redirect('main:employees')


@login_required(login_url='main:login')
def report_full(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'xisobot/full.html', context)


@login_required(login_url='main:login')
def report_by_department(request, pk):
    department = Department.objects.get(pk=pk)
    employees = Employee.objects.filter(department=department)
    context = {'employees': employees, 'department': department}
    return render(request, 'xisobot/by_department.html', context)


@login_required(login_url='main:login')
def report_by_type(request, pk):
    pc_type = Type.objects.get(pk=pk)
    employees = Employee.objects.filter(computer__type=pc_type)
    context = {'employees': employees, 'type': pc_type}
    return render(request, 'xisobot/by_type.html', context)


@login_required(login_url='main:login')
def report_active_computer(request):
    computers = Computer.objects.filter(is_active=True)
    context = {'computers': computers}
    return render(request, 'xisobot/active_pc.html', context)


@login_required(login_url='main:login')
def report_deactivate_computer(request):
    computers = Computer.objects.filter(is_active=False)
    context = {'computers': computers}
    return render(request, 'xisobot/deactive_pc.html', context)
