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
    path('mine/', views.mine, name = 'mine'),
    path('result/', views.result, name = 'result'),
    path('table', views.person_list, name = 'table'),
    path('export/', export_data, name="export"),
    
   


]

urlpatterns += router.urls
















