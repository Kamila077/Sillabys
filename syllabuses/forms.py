from django import forms
from .models import Literature, Syllabus, School, CustomUser, Director

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['title']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'prof']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['full_name', 'prof', 'school']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'prof', 'password']  # Укажите поля, которые вы хотите отображать на форме



class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = [
            'syllabus_name',
            'course',
            'training_level',
            'language_of_education',
            'proficiency_level',
            'total_hours',
            'classroom_hours',
            'semester',
            'ects',
            'iw_hours',
            'prerequisites',
            'format_of_training',
            'edu_programms',
            'time_place',
            'instructor',
            'course_objective',
            'agreed_with',
            'asu',
        ]
        widgets = {
            'prerequisites': forms.Textarea(attrs={'rows': 1, "class": "form-control"}),
            'edu_programms': forms.Textarea(attrs={'rows': 1, "class": "form-control"}),
            'time_place': forms.Textarea(attrs={'rows': 1, "class": "form-control"}),
            'course_objective': forms.Textarea(attrs={'rows': 1, "class": "form-control"}),
            'syllabus_name': forms.TextInput(attrs={'rows': 1, "class": "form-control"}),
            'course': forms.Select(attrs={'rows': 2, "class": "form-select"}),
            'training_level': forms.Select(attrs={'rows': 2, "class": "form-control"}),
            'language_of_education': forms.Select(attrs={'rows': 2, "class": "form-control"}),
            'proficiency_level': forms.Select(attrs={'rows': 2, "class": "form-control"}),
            'total_hours': forms.NumberInput(attrs={'rows': 1, "class": "form-control"}),
            'classroom_hours': forms.NumberInput(attrs={'rows': 1, "class": "form-control"}),
            'ects': forms.NumberInput(attrs={'rows': 1, "class": "form-control"}),
            'semester': forms.NumberInput(attrs={'rows': 1, "class": "form-control"}),
            'iw_hours': forms.NumberInput(attrs={'rows': 1, "class": "form-control"}),
            'format_of_training': forms.Select(attrs={'rows': 2, "class": "form-control"}),
            'edu_programms': forms.Textarea(attrs={'rows': 1, "class": "form-control"}),
            'instructor': forms.Select(attrs={'rows': 2, "class": "form-control"}),
            'agreed_with': forms.Select(attrs={'rows': 2, "class": "form-control"}),
            # 'asu': forms.Textarea(attrs={'rows': 1, "class": "form-control"}),


        }


class SecondStepForm(forms.ModelForm):
    class Meta:
        model = Literature
        fields = ['course','title']
        labels = {
            'course': 'Дисциплина',
        
            'title': 'Название',
        }

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', None)
        super(SecondStepForm, self).__init__(*args, **kwargs)
        if course:
            self.fields['course'].initial = course