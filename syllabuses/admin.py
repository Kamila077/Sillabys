from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class StuAdmin(UserAdmin):
     model = CustomUser
     list_display = (
        'username', 'email', 'first_name', 'last_name', 'prof',
    )
     fieldsets = (
        (None, {'fields': ('email', 'password', 'prof')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, StuAdmin)

admin.site.register(School)

admin.site.register(Director)
admin.site.register(Course)
admin.site.register(Status)
admin.site.register(EduLevel)
admin.site.register(Proficiency)
admin.site.register(Language)
admin.site.register(Format)
admin.site.register(Syllabus)
admin.site.register(Literature)
admin.site.register(Module)
admin.site.register(LiteratureInSyllabus)
admin.site.register(CourseLO)
