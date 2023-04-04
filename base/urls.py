from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name = "register"),
    path('student', views.studentPage, name='student'),
    path('student_find_tutor', views.studentFindTutor, name='student_find_tutor'),
    path('student_request_tutor', views.studentFindTutor, name='student_request_tutor'),
    path('tutor', views.tutorPage, name='tutor'),
    path('course-posting', views.postCourses, name='course-posting'),
    path('course-searching', views.courseLookup, name='course-searching'),
]

