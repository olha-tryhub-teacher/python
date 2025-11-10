from django.urls import path

from school.views import (home,
                          teachers,
                          teacher,
                          students,
                          student,
                          classrooms,
                          classroom_detail)

urlpatterns = [
    path("home/", home, name="school-home"),
    path("teachers/", teachers, name="school-teachers"),
    path("teacher/<int:pk>/", teacher, name="school-teacher"),
    path("students/", students, name="school-students"),
    path("student/<int:pk>/", student, name="school-student"),
    path("classrooms/", classrooms, name="school-classrooms"),
    path("classroom/<int:pk>/", classroom_detail, name="school-classroom-detail"),
]

app_name = "school"