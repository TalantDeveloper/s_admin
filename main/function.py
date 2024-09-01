from .models import Type, Computer, Department, Employee


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
