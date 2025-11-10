from django.db import models

# Create your models here.
from django.db import models

# Таблиця Вчитель
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)   # Ім'я
    last_name = models.CharField(max_length=100)    # Прізвище
    salary = models.DecimalField(max_digits=8, decimal_places=2)  # Зарплата

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# Таблиця Клас
class Classroom(models.Model):
    start_year = models.IntegerField()              # Рік початку навчання (наприклад 2021)
    letter = models.CharField(max_length=1)         # Літера класу (А, Б, В...)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')

    def __str__(self):
        return f"{self.start_year}-{self.letter}"


# Таблиця Учень
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()                  # Дата народження
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

