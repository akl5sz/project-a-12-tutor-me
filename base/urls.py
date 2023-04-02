from django.urls import path

from . import views
#from .views import SearchResultsView

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name = "register"),
    path('student', views.studentPage, name='student'),
    path('tutor', views.tutorPage, name='tutor'),
    path('courses', views.coursePage, name='courses'),
    #path('search/', SearchResultsView.as_view(), name='search_results'),

]

