from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts import serializers

@api_view(["POST"])
def create_view(request):
	if request.is_ajax() and request.method == "POST":
		data = {
			"email": request.data.get("email", None),
		}
		user_serializer = serializers.UserSerializer(data=data)
		if user_serializer.is_valid():
			user_serializer.save()
			return Response(user_serializer.data)
		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	raise Http404