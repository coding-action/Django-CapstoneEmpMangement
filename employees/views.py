from django.shortcuts import render, redirect  
from employees.forms import EmployeeForm  
from employees.models import Employee  
from django.views import View
# Create your views here.  
class emp(View):
    def post(self, request):  
        if request.method == "POST":  
            form = EmployeeForm(request.POST, request.FILES)   
            if form.is_valid():  
                try:  
                    form.save() 
                    return redirect('/show')  
                except:  
                    pass  
        else:  
            form = EmployeeForm()  
            return render(request,'index.html',{'form':form}) 
    def get(self, request):  
        if request.method == "POST":  
            form = EmployeeForm(request.POST, request.FILES)   
            if form.is_valid():  
                try:  
                    form.save() 
                    return redirect('/show')  
                except:  
                    pass  
        else:  
            form = EmployeeForm()  
            return render(request,'index.html',{'form':form}) 
class show(View):
    def get(self, request):  
        employees = Employee.objects.all()  
        return render(request,"show.html",{'employees':employees})  
class edit(View):
    def get(self, request, id):  
        employee = Employee.objects.get(id=id)  
        return render(request,'edit.html', {'employee':employee}) 
class update(View):
    def post(self, request, id):  
        employee = Employee.objects.get(id=id)  
        form = EmployeeForm(request.POST, request.FILES, instance = employee) 
        if form.is_valid(): 
            form.save() 
            return redirect("/show")  
        {{form.error_class}}
        return render(request, 'edit.html', {'employee': employee})  
class details(View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)  
        return render(request, 'details.html', {'employee': employee}) 
class destroy(View):
    def get(self, request, id):  
        employee = Employee.objects.get(id=id)  
        employee.delete()  
        return redirect("/show")  