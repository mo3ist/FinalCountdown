from django.contrib import admin

class ExamAdmin(admin.ModelAdmin):
	list_display = ['__str__']

class ActivityAdmin(admin.ModelAdmin):
	list_display = ['__str__']