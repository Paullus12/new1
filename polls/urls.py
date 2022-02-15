from django.urls import path

from . import views
from rest_framework.routers import SimpleRouter
from .models import Student
from .views import StudentView
from .views import LanguageView
from .views import EmploymentView
from .views import ThemeView
from .views import export_data
from rest_framework import routers
from django.conf.urls import url, include


router = SimpleRouter()
router.register('api/students', StudentView)
router.register('api/languages', LanguageView)
router.register('api/employment', EmploymentView)
router.register('api/theme', ThemeView)




urlpatterns = [
    path('', views.index, name='home'),
    path('creat',views.creat, name='creat'),
    path('table', views.table, name = 'table'),
    path('result/', views.result, name = 'result'),
    path('export/', export_data, name="export"),
    path('login', views.login, name="login"),

    
   


]

urlpatterns += router.urls
















