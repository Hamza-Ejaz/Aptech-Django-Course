from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Employees
from .models import Employee
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  


class employeeviews(APIView):
    def post(self, request):
        serializer = Employee(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status.HTTP_400_BAD_REQUEST)    

    def get(self,request,id=None):
        if id:
            item = Employee.objects.get(id=id)
            serializer =Employees(item)
            return Response({"status":"success","data":serializer.data},status.HTTP_200_OK)

        items = Employee.objects.all()
        serializer =Employees(items,many=True)
        return Response({"status":"success","data":serializer.data},status.HTTP_200_OK)
