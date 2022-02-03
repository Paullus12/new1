from attr import field
import django_filters

from .models import*

class AllFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['name']