from django.db.models import fields
import django_tables2 as tables
from .models import *

class StudentTable(tables.Table):
    class Meta:
        model = Student
        fields = ['name','surname','group','work','info','employment','language','expirience','theme1','theme2','theme3','theme4']