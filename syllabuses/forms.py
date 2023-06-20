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
            'prerequisites': forms.Textarea(attrs={'rows': 4}),
            'edu_programms': forms.Textarea(attrs={'rows': 4}),
            'time_place': forms.Textarea(attrs={'rows': 4}),
            'course_objective': forms.Textarea(attrs={'rows': 4}),
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