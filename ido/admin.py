from django.contrib import admin
from .models import liveData,memberData,historicalRecord,covidRecord
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class liveDataCustom(admin.ModelAdmin):
    list_display = ['name','major','student_num', 'enter_time']
    ordering = ['enter_time']
    list_filter = ['name']
    search_fields =['name']


class memberDataCustom(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name','major','student_num', 'reserve_date','reserve_product','email']
    ordering = ['reserve_date']
    list_filter = ['name']
    search_fields =['name']
    pass

class historicalRecordCustom(admin.ModelAdmin):
    list_display = ['name','major','student_num', 'reserve_date','reserve_product','email']
    ordering = ['reserve_date']
    list_filter = ['name']
    search_fields =['name']

class covidRecordCustom(admin.ModelAdmin):
    list_display = ['name','major','student_num', 'enter_time']
    ordering = ['enter_time']
    list_filter = ['name']
    search_fields =['name']



admin.site.register(liveData,liveDataCustom)
admin.site.register(memberData,memberDataCustom)
admin.site.register(historicalRecord,historicalRecordCustom)
admin.site.register(covidRecord,covidRecordCustom)

