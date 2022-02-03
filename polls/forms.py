from django import forms
from django.db.models import fields
from .models import Employment, Student, Language, Expirience, Theme, Teacher
from django.forms import ModelForm
from django.forms import Form


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employment'].empty_label = 'Сделайте выбор'
        self.fields['theme1'].empty_label = 'Сделайте выбор'
        self.fields['theme2'].empty_label = 'Сделайте выбор'
        self.fields['theme3'].empty_label = 'Сделайте выбор'
        self.fields['theme4'].empty_label = 'Сделайте выбор'

    class Meta:
        model = Student
        fields = ['name','surname','group','work','info','employment','theme1','theme2','theme3','theme4','language','expirience']
        widgets = {

            'name':forms.TextInput(attrs={'class':'form-input'}),
            
            'info':forms.Textarea(),
            
        }

    
    
    
    
    
    
    
    
    
    
    
"""
    
    
    name = forms.CharField(max_length=50,label="Имя", widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(max_length=50,label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-input'}))
    group = forms.CharField(max_length=50,label="Группа", widget=forms.TextInput(attrs={'class': 'form-input'}))
    work = forms.CharField(max_length=50,label="Место работы", widget=forms.TextInput(attrs={'class': 'form-input'}))
    info = forms.CharField(max_length=50,label="Дополнительная информация", widget=forms.TextInput(attrs={'class': 'form-input'}))
	#expirience = models.ManyToManyField('Expirience',through='StudentExpirience')
    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all())
    employment = forms.ModelChoiceField(queryset=Employment.objects.all(), label="Занятость", empty_label="Категория не выбрана")
    theme1 = forms.ModelChoiceField(queryset=Theme.objects.all(), label="Тема1", empty_label="Категория не выбрана")
    theme2 = forms.ModelChoiceField(queryset=Theme.objects.all(), label="Тема2", empty_label="Категория не выбрана")
    theme3 = forms.ModelChoiceField(queryset=Theme.objects.all(), label="Тема3", empty_label="Категория не выбрана")
    theme4 = forms.ModelChoiceField(queryset=Theme.objects.all(), label="Тема4", empty_label="Категория не выбрана")


"""









