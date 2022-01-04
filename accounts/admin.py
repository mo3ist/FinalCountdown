from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

class UserAdmin(BaseUserAdmin):
	list_display = ["__str__"]

	fieldsets = (
		(None, {'fields': ('name', 'email', 'password', 'is_staff',)}),
	)

	add_fieldsets = (
		(None, {'fields': ('email', 'password1', 'password2', 'is_staff')}),
	)

	filter_horizontal = []

	list_filter = []
	
	ordering = ['email']

UserModel = get_user_model()

admin.site.register(UserModel, UserAdmin)