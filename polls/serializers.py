from os import read
from rest_framework.serializers import ModelSerializer
from .models import Student, Language, Employment, Theme




class ThemeSerializer(ModelSerializer):
	class Meta:
		model = Theme
		fields = '__all__'


class StudentSerializer(ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
		




class LanguageSerializer(ModelSerializer):
	class Meta:
		model = Language
		fields = '__all__'



class EmploymentSerializer(ModelSerializer):
	class Meta:
		model = Employment
		fields = '__all__'







