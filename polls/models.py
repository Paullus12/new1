from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, SlugField
from django.db.models.fields.related import ManyToManyField




class Direction(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True, default='default')
	

	def __str__(self) :
		return self.name or ''


class Teacher(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True, default='default')
	

	def __str__(self) :
		return self.name or ''


class Theme(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	

	def __str__(self):
		return self.name


class Student(models.Model):
	name = models.CharField(max_length=50,verbose_name="Имя")
	surname = models.CharField(max_length=50,verbose_name="Фамилия")
	group = models.CharField(max_length=50,verbose_name="Группа")
	work = models.CharField(max_length=50,verbose_name="Место работы")
	info = models.CharField(max_length=50,verbose_name="Дополнительная информация о себе")
	expirience = models.ManyToManyField('Expirience',blank=True,verbose_name="Программы")
	employment = models.ForeignKey('Employment', on_delete=CASCADE, related_name='employment', null=True,verbose_name="Чем Вы сейчас занимаетесь")
	language = models.ManyToManyField('Language', blank=True,verbose_name="Языки программирования")
	theme1 = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='theme1', null=True,verbose_name="Тема1")
	theme2 = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='theme2', null=True,verbose_name="Тема2")
	theme3 = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='theme3', null=True,verbose_name="Тема3")
	theme4 = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='theme4', null=True,verbose_name="Тема4")

	def __str__(self):
		return "{} {} {} {} {}".format(self.surname, self.name, self.group, self.work, self.info)
				
		
class Employment(models.Model):

	name = models.CharField(max_length = 100, null=True, blank=True, default = 'default')
	
	def __str__ (self):
		return self.name or ''


class Expirience(models.Model):

	name = models.CharField(max_length=15, null=True, default='default')
	
									
	def __str__ (self):
		return self.name or ''

class Language(models.Model):

	name = models.CharField(max_length=8, null=True,blank=True, default='default')
	
	
	def __str__ (self):
		return self.name or ''































		

