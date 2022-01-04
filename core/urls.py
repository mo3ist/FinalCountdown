from core import views
from django.urls import path

urlpatterns = [
	path('', views.home_view)
]