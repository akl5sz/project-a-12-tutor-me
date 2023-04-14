from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.registerPage, name = "register"),

    path('student-home', views.studentHome, name='student-home'),
    path('student-find-tutor', views.studentFindTutor, name='student-find-tutor'),
    path('student-request-tutor', views.studentTutorSearch, name='student-request-tutor'),
    path('student-submit-request', views.studentSubmitRequest, name='student-submit-request'),

    path('tutor-home', views.tutorHome, name = 'tutor-home'),
    path('tutor-post-rate', views.tutorPostRate, name='post-rate'),
    path('tutor-view-rate', views.tutorViewRate, name='view-rate'),
    path('tutor-view-courses', views.tutorViewCourses, name='tutor-view-courses'),
    path('tutor-post-courses', views.tutorPostCourses, name='tutor-post-courses'),
    path('tutor-remove-courses', views.tutorRemoveCourses, name='tutor-remove-courses'),

    path('tutor-course-lookup', views.tutorCourseLookup, name='tutor-course-lookup'),
    path('student-course-lookup', views.studentCourseLookup, name='student-course-searching'),

    path('search/', views.SearchResultsView, name='search_results'),
]