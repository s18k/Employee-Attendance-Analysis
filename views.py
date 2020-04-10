from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
def index(request):
    employees=Employee.objects.all()

    print(employees)
    params={'employee':employees}
    return render(request,'analysis/index.html',params)
def about(request):
    return render(request,'analysis/about.html')



def search(request):
    query=request.GET.get('search')

    emp=Employee.objects.get(employee_name=query).employee_position
    print(emp)


    return HttpResponse(request,"Search")