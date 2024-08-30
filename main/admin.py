from django.contrib import admin
from .models import Type, Computer, Department, Employee


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name',)
    empty_value_display = '-empty-'


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'invention_id', 'type', 'is_active', 'years')
    list_display_links = ('id', 'invention_id', 'type', 'is_active', 'years')
    search_fields = ('id', 'invention_id', 'type', 'is_active', 'years')
    list_filter = ('id', 'invention_id', 'type', 'is_active', 'years')
    empty_value_display = '-empty-'


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name',)
    empty_value_display = '-empty-'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'department', 'computer')
    list_display_links = ('id', 'full_name', 'department', 'computer')
    search_fields = ('id', 'full_name', 'department', 'computer')
    list_filter = ('id', 'department')
    empty_value_display = '-empty-'


admin.site.register(Type, TypeAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
