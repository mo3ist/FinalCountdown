from django.urls import path, include

from accounts import views 

urlpatterns = [
	path('create/', views.create_view)
]
