from django.urls import path, include

from accounts import views 

urlpatterns = [
	path('subscribe/', views.subscribe_view),
	path('unsubscribe/', views.unsubscribe_view)
]
