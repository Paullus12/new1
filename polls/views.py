from datetime import date
from typing import Union
from django.db.models import query
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from polls.models import Student, Language, Expirience, Theme, Teacher, Employment
from django.http import HttpResponse
from .forms import StudentForm
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from polls.serializers import StudentSerializer
from polls.serializers import LanguageSerializer
from polls.serializers import EmploymentSerializer
from polls.serializers import ThemeSerializer
from django.views.generic.list import ListView
from rest_framework import viewsets
from polls.tables import *
from .resources import StudentResource
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport
from django.db import connection
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from collections import Counter
from django_filters.views import FilterView
from .filters import AllFilter
from collections import OrderedDict
import collections
from dataclasses import dataclass, fields




def index(request):
	return render(request, "polls/index.html")


def creat(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('creat')
	else:
		form = StudentForm()
		return render(request, 'polls/creat.html',{'form':form})


def table(request):
    
    
    

    """y = Counter(y)
    print(y)
    for kay, value in y.items():
        x.append({'name':kay,'value':value})

    print(x)"""
	
    qs = Student.objects.values('id','name','surname','group','info','work','expirience__name','employment__name','language__name','theme1__name','theme1__direction__name','theme2__direction__name','theme3__direction__name','theme4__direction__name','theme2__name','theme3__name','theme4__name')
    print(qs)

    @dataclass
    class User:
        id: list
        name: list
        surname: list
        group: list
        info: list
        work: list
        expirience__name: list
        employment__name: list
        language__name: list
        theme1__name: list
        theme1__direction__name: list
        theme2__name: list
        theme2__direction__name: list
        theme3__name: list
        theme3__direction__name: list
        theme4__name: list
        theme4__direction__name: list

        def __repr__(self) -> str:
            pass

        def __str__(self):
            pass


    def sort_users(data):
        users_list = []  # список для будущего хранения списка пользователей

        # конвертируем value словаря в list
        for item in data:
            user_dict = {k: [v] for k, v in item.items()}
            

            # если список users_list пустой, добавить первый элемент для работы
            if len(users_list) <= 0:
                user = User(**user_dict)
                users_list.append(user)
                
            # итерируем список users_list содержащий экземпляры Users
            for user in users_list:
                if user_dict.get('id') not in [user.id for user in users_list]:  # проверим, что ID уникален в списке
                    users_list.append(User(**user_dict))
                else:
                    for field in fields(user):
                        field_value: list = getattr(user, field.name)
                        user_value: list = user_dict.get(field.name)
                        if user_dict.get('id')[0] == user.id[0]:
                            if user_value[0] not in field_value:
                                field_value.append(user_value[0])

        # тут мы из списка с датаклассом форматируем код и выводим словарь
        formatted_users_list = []
        for user in users_list:
            _dict = {}
            for field in fields(user):
                _dict[field.name] = ','.join(str(x) for x in getattr(user, field.name))
            formatted_users_list.append(_dict)

        return formatted_users_list

    
    qs1 = sort_users(data=qs)
   

    d={}
    l=[]



    return render(request, 'polls/table.html', {'st':qs1})

"""
class ClubCharViwe(TemplateView):


    template_name = 'polls/result.html'
    def get_context(self, **kwargs):
        context = suoer().get_gontext(**kwargs)
        context["qs"] = Club_objects.all()
        return context
"""

def result(request):
   
    
    teacher=[]
    t = Teacher.objects.values()
    for i in t:
        teacher.append(i['name'])
    
    
    val = []
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    
    d1={}
    d2={}
    d3={}
    d4={}
    
    qs = Student.objects.values('theme1__teacher__name','theme2__teacher__name','theme3__teacher__name','theme4__teacher__name')
    
    for i in qs:
        t1.append(i['theme1__teacher__name'])
        t2.append(i['theme2__teacher__name'])
        t3.append(i['theme3__teacher__name'])
        t4.append(i['theme4__teacher__name'])
    t1=list(zip(*Counter(t1).items()))
    t2=list(zip(*Counter(t2).items()))
    t3=list(zip(*Counter(t3).items()))
    t4=list(zip(*Counter(t4).items()))
    tt1 = dict(zip(t1[0], t1[1]))
    tt2 = dict(zip(t2[0], t2[1]))
    tt3 = dict(zip(t3[0], t3[1]))
    tt4 = dict(zip(t4[0], t4[1]))

    

    for i in qs:
        for kay, value in i.items():
            val.append(value)
    result = list(zip(*Counter(val).items()))
    tt = dict(zip(result[0], result[1]))
    tt = collections.OrderedDict(sorted(tt.items()))
    
    for k in teacher:
        if k in tt1:
            d1[k]=tt1[k]
        else: d1[k] = 0
    d1 = collections.OrderedDict(sorted(d1.items()))

    for k in teacher:
        if k in tt2:
            d2[k]=tt2[k]
        else: d2[k] = 0
    d2 = collections.OrderedDict(sorted(d2.items()))

    for k in teacher:
        if k in tt3:
            d3[k]=tt3[k]
        else: d3[k] = 0
    d3 = collections.OrderedDict(sorted(d3.items()))

    for k in teacher:
        if k in tt4:
            d4[k]=tt4[k]
        else: d4[k] = 0
    d4 = collections.OrderedDict(sorted(d4.items()))


    

    """y = Counter(y)
    print(y)
    for kay, value in y.items():
        x.append({'name':kay,'value':value})

    print(x)"""

    

    return render(request,'polls/result.html',{'stud': tt, 'tn1':d1,'tn2':d2, 'tn3':d3,'tn4':d4})
    
    


class StudentView(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get_options(self):
		return "options",{
			"employment":[{'lable':obj.name, 'value':obj.pk} for obj in Employment.objects.all()]

		}

	class Meta:
		datatables_extra_json = ('get_options',)





class LanguageView(ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer


class EmploymentView(ModelViewSet):
	queryset = Employment.objects.all()
	serializer_class = EmploymentSerializer


class ThemeView(ModelViewSet):
	queryset = Theme.objects.all()
	serializer_class = ThemeSerializer


    

def export_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        student_resource = StudentResource()
        dataset = student_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'export.html')















