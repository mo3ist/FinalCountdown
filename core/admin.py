from django.contrib import admin
from core import models

class ExamAdmin(admin.ModelAdmin):
	list_display = ['__str__']

class ActivityAdmin(admin.ModelAdmin):
	list_display = ['__str__']


admin.site.register(models.Exam, ExamAdmin)
admin.site.register(models.Activity, ActivityAdmin)