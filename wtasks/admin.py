from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['Name', 'Assigned_Task', 'Task_Status', 'Salary']
admin.site.register(Employee, EmployeeAdmin)