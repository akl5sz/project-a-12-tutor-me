from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name = "register"),
    path('student', views.studentPage, name='student'),
    path('tutor', views.tutorPage, name='tutor'),
    path('course-posting', views.postCourses, name='course-posting'),
    path('course-searching', views.courseLookup, name='course-searching'),
]

