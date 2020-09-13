from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def addnew(request):
    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'wtasks/index.html', {'form': form}) 


def show_view(request):
    employees = Employee.objects.all()
    return render(request, 'wtasks/show.html', {'employees': employees})

def delete_view(request,id):
    employees = Employee.objects.get(id=id)
    employees.delete
    return redirect('/')

def update_view(request,id):
    employees = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance= employees)
    if form.is_valid():
        form.save(commit= True)
        return redirect('/')
    return render(request, 'wtasks/edit.html', {'employees': employees})