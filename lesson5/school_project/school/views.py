from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render #⬅️⬅️⬅️

from school.models import Teacher, Student, Classroom

def home(request):
    # return HttpResponse("Привіт, це мій перший сайт на Django!")
    return render(request, 'home.html') #⬅️⬅️⬅️

def teachers(request):
    teachers_obj = Teacher.objects.all()
    # return HttpResponse(teachers_obj)
    context = {'teachers': teachers_obj} #⬅️⬅️⬅️
    return render(request, 'teachers.html', context) #⬅️⬅️⬅️

def teacher(request, pk):
    teacher_obj = Teacher.objects.filter(id=pk).first()
    # return HttpResponse(teacher_obj)
    context = {'teacher': teacher_obj} #⬅️⬅️⬅️
    return render(request, 'teacher.html', context) #⬅️⬅️⬅️

def students(request):
    students_obj = Student.objects.all()
    return HttpResponse(students_obj)

def student(request, pk):
    student_obj = Student.objects.filter(id=pk)
    return HttpResponse(student_obj)

def classrooms(request):
    classrooms_obj = Classroom.objects.all()
    return HttpResponse(classrooms_obj)


def classroom_detail(request, pk):
    classroom = Classroom.objects.get(id=pk)  # Отримуємо конкретний клас
    teacher = classroom.class_teacher
    students = classroom.students.all()       # Завдяки related_name='students'

    # Формуємо текстовий результат
    response = f"<h2>Клас: {classroom}</h2>"
    response += f"<p>Класний керівник: {teacher.first_name} {teacher.last_name}</p>"
    response += "<h3>Список учнів:</h3><ul>"

    for s in students:
        response += f"<li>{s.first_name} {s.last_name}</li>"
    response += "</ul>"

    return HttpResponse(response)