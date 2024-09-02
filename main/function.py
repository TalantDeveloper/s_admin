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

