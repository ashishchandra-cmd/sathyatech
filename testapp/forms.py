from django import forms
from testapp.models import Course_table

class Course_tableForm(forms.ModelForm):
    class Meta:
        model=Course_table
        fields=['Course_Name','Faculty','class_date','class_time','Fee','Duration']