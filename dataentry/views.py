# views.py
from django.core.management import call_command
from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.conf import settings
from django.contrib import messages
from .models import Student, Customer, Employee


def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')

        # Store this file inside the upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        # Build the file path
        relative_path = upload.file.url
        base_url = str(settings.BASE_DIR)
        file_path = base_url + relative_path

        # Trigger the Celery task
        try:
            call_command('importdata', file_path, model_name)
        except Exception as e:
            messages.error(request,str(e))

        # Show message to the user
        messages.success(request, "Your data is  imported.")
        return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models
        }
        return render(request, 'dataentry/importdata.html', context)
def export_data(request):
    if request.method=='POST':
        model_name=request.POST.get('model_name')
        try:
            call_command('exportdata',model_name)
        except Exception as  e:
            raise e
        messages.success(request,"Your data is Exported")
        return redirect('export_data')
    else:
        custom_models=get_all_custom_models()
        context={
            'custom_models':custom_models,
        }
    return render(request,'dataentry/exportdata.html',context)
def viewdata(request):
    table = request.GET.get('table', 'student')  # Default to 'student'
    search_query = request.GET.get('search', '')

    if table == 'student':
        data = Student.objects.filter(name__icontains=search_query)
        seen_names = set()
        unique_data = []
        for student in data:
            if student.name not in seen_names:
                unique_data.append(student)
                seen_names.add(student.name)
        columns = ['Roll No', 'Name', 'Age']
    elif table == 'customer':
        data = Customer.objects.filter(customer_name__icontains=search_query)
        seen_customers = set()
        unique_data = []
        for customer in data:
            if customer.customer_name not in seen_customers:
                unique_data.append(customer)
                seen_customers.add(customer.customer_name)
        columns = ['Customer Name', 'Country']
    elif table == 'employee':
        data = Employee.objects.filter(employee_name__icontains=search_query)
        seen_employees = set()
        unique_data = []
        for employee in data:
            if employee.employee_name not in seen_employees:
                unique_data.append(employee)
                seen_employees.add(employee.employee_name)
        columns = ['Employee ID', 'Employee Name', 'Designation', 'Salary', 'Retirement', 'Other Benefits', 'Total Benefits', 'Total Compensation']
    else:
        unique_data = []  # Default empty data

    # Calculate colspan
    colspan = len(columns) + 1  # Adding 1 for the Actions column

    context = {
        'data': unique_data,
        'columns': columns,
        'selected_table': table,
        'search_query': search_query,
        'colspan': colspan,  # Pass colspan to the template
    }
    return render(request, 'table.html', context)