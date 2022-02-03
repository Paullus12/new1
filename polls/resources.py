from django.db.models import fields
from import_export import resources, fields, widgets
from .models import Employment, Student, Language, Expirience, Theme, Teacher
import json

from django.core import serializers
from import_export.widgets import JSONWidget, ManyToManyWidget, ForeignKeyWidget



"""

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
       
"""
        



class StudentResource(resources.ModelResource):
   

    expirience = fields.Field(
        attribute='expirience',
        widget=ManyToManyWidget(model=Expirience, separator=',', field='name'),
    )
    
    
    language = fields.Field(
        attribute='language',
        widget=ManyToManyWidget(model=Language, separator=',', field='name'),
    )


    employment = fields.Field(
        attribute='employment',
        widget=ForeignKeyWidget(model=Employment, field = 'name'),
    )
    theme1 = fields.Field(
        attribute='theme1',
        widget=ForeignKeyWidget(model=Theme, field = 'name'),
   
    )
    theme2 = fields.Field(
        attribute='theme2',
        widget=ForeignKeyWidget(model=Theme, field = 'name'),
   
    )
    theme3 = fields.Field(
        attribute='theme3',
        widget=ForeignKeyWidget(model=Theme, field = 'name'),
   
    )
    theme4 = fields.Field(
        attribute='theme4',
        widget=ForeignKeyWidget(model=Theme, field = 'name'),
   
    )


    class Meta:
        model = Student
        export_order = ('id', 'name', 'surname','group','work','info')
        