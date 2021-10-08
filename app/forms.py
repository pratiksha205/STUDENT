from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id','student_name','roll_number','birth_date','joining_date')
