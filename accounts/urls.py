from django.urls import path, include

from accounts import views 

urlpatterns = [
	path('subscripe/', views.subscripe_view),
	path('unsubscripe/', views.unsubscripe_view)
]
