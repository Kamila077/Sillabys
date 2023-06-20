from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    title = models.CharField('Название школы', max_length=255)

    def __str__(self):
        return f"{self.id} {self.title}"

class CustomUser(AbstractUser):
    email = models.EmailField('Эл. Почта', max_length=255)
    prof = models.CharField('Должность', max_length=255)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}."

    def __str__(self):
        return self.get_full_name()

    def get_created_syllabuses(self):
        return Syllabus.objects.filter(instructor=self)

    class Meta:
        verbose_name = 'Преподаватель'

    



class Director(models.Model):
    full_name = models.CharField('ФИ', max_length=255)
    prof = models.CharField('Должность', max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField('Название дисциплины', max_length=255)
    code = models.CharField('Код', max_length=255)

    def __str__(self):
        return f"{self.code} {self.name}"


class Status(models.Model):
    type = models.CharField('Статус', max_length=255)

    def __str__(self):
        return f"Статус {self.type}"

class EduLevel(models.Model):
    type = models.CharField('Уровень обучения', max_length=255)

    def __str__(self):
        return f"{self.type}"


class Proficiency(models.Model):
    level = models.CharField('Знание языка', max_length=255)

    def __str__(self):
        return f"{self.level}"


class Language(models.Model):
    title = models.CharField('Язык', max_length=255)

    def __str__(self):
        return f"{self.title}"


class Format(models.Model):
    type = models.CharField('формат', max_length=255)

    def __str__(self):
        return f"{self.type}"
    
class Syllabus(models.Model):
    syllabus_name = models.CharField('Название силлабуса', max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, verbose_name='Дисциплина')
    training_level = models.ForeignKey(EduLevel, on_delete=models.CASCADE, null=True, verbose_name='Уровень обучения')
    language_of_education = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, verbose_name='Язык обучения')
    proficiency_level = models.ForeignKey(Proficiency, on_delete=models.CASCADE, null=True, verbose_name='Уровень владения языком')
    total_hours = models.IntegerField('Всего часов', null=True)
    classroom_hours = models.IntegerField('Классных часов', null=True)
    semester=models.IntegerField('Семестр', null=True)
    ects = models.IntegerField('ects кредиты', null=True)
    iw_hours = models.IntegerField('СРОП часов', null=True)
    prerequisites = models.TextField('Пререквизиты', blank=False)
    format_of_training = models.ForeignKey(Format,on_delete=models.CASCADE, null=True, verbose_name='Формат обучения')
    edu_programms = models.TextField('Образовательные программы', blank=False)
    time_place = models.TextField('Время и место проведения',blank=False)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, verbose_name='Инструктор/Преподаватель')
    course_objective = models.TextField('Цель курса',blank=False)
    document = models.FileField('Файл', null=True, blank=True)
    agreed_with = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, verbose_name='Согласовывает: ')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    course_philosophy = models.TextField('Философия курса', blank=False)
    course_etics = models.TextField('Политика курса', blank=False)
    asu = models.BooleanField('На основе ASU', default=0)

    def __str__(self):
        return f"{self.syllabus_name}, {self.course}, {self.language_of_education}"
    

class Literature(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, verbose_name='Дисциплина', related_name='literature_set')
    title = models.TextField('Название', blank=False)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, null=True, verbose_name='Силлабус', related_name='literature_set')

    def __str__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}."
    

#Создаем связь с силлабусом для добавления обяз и необяз литературы
class LiteratureInSyllabus(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, null=True, verbose_name='Силлабус')
    literature = models.ForeignKey(Literature, on_delete=models.CASCADE, null=True, verbose_name='Литература')
    mandatory = models.BooleanField('Обязательная', default=0)

    def __str__(self):
        return f"{self.literature}."



class CourseLO(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, null=True, verbose_name='Силлабус')
    type = models.BooleanField('Тип РО', default=0)
    info = models.TextField('Результаты обучения', blank=False)

class Module(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, null=True)
    week = models.IntegerField('Неделя', null=True)
    theme = models.TextField('Тема', blank=False)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    tasks = models.TextField('Задания', blank=False)
    course_lo = models.TextField('Результаты обучения', blank=False)
    questions = models.TextField('Вопросы по модулю', blank=False)
    literature = models.ForeignKey(LiteratureInSyllabus, on_delete=models.CASCADE, null=True)
    grading = models.TextField('Оценивание', blank=False)
    max_percent = models.IntegerField('Максимальный процент', null=True)
    max_weight = models.IntegerField('Максимальный вес', null=True)
    total_in_points = models.IntegerField('В баллах', null=True)
    def __str__(self):
        return f"{self.week} неделя, {self.theme}"
