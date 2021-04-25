from django import forms  
from employees.models import Employee 

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__" 
        widgets = {
            'checkgender': forms.RadioSelect(),
            'dob': forms.SelectDateWidget(years=[x for x in range(1940,2021)]),
        }
       
