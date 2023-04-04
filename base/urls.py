from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name = "register"),
    path('student', views.studentPage, name='student'),
    path('student-find-tutor', views.studentFindTutor, name='student-find-tutor'),
    path('student-request-tutor', views.studentTutorSearch, name='student-request-tutor'),


    path('tutor-home', views.tutorHome, name = 'tutor-home'),

    path('post-rate', views.postRate, name='post-rate'),
    path('view-rate', views.viewRate, name='view-rate'),

    path('tutor-view-courses', views.viewCourses, name='tutor-view-courses'),
    path('tutor-post-courses', views.postCourses, name='tutor-post-courses'),

    path('course-searching', views.courseLookup, name='course-searching'),
]

