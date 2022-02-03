from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Student, Language, Theme, Teacher,  Employment, Expirience,Direction


admin.site.register(Student)
admin.site.register(Language)
admin.site.register(Expirience)
admin.site.register(Teacher)
admin.site.register(Employment)
admin.site.register(Theme)
admin.site.register(Direction)




