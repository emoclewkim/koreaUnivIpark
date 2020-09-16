from django.contrib import admin
from .models import Survey

class customAdmin(admin.ModelAdmin):
    list_display = ['name', 'major', 'update_time']


admin.site.register(Survey, customAdmin)

# Register your models here.
