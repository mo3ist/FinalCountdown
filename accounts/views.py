from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from accounts import serializers
from accounts import models
from conf.celery import send_initial_email_task, send_goodluck_email_task
from core import models as core_models

@api_view(["POST"])
def subscripe_view(request):
	if request.is_ajax() and request.method == "POST":
		data = {
			"email": request.data.get("email", None),
		}

		try:

			user = models.User.objects.get(email=data["email"])

			if not user.is_subbed:
				user.is_subbed = True
				user.save()

			print(f"{user.is_subbed=}")

			return Response(status=status.HTTP_200_OK)

		except:

			user_serializer = serializers.UserSerializer(data=data)
			if user_serializer.is_valid(raise_exception=True):
				user = user_serializer.save()

				# Send an initial sub email
				send_initial_email_task.delay(user.email)

				print("SENT")

				# Send a goodluck email before each exam 
				# sorted by due_date
				for exam in core_models.Exam.objects.all():
					after_1_hour = timezone.now() + timezone.timedelta(minutes=1)

					hour_before_due = exam.due_date - timezone.timedelta(minutes=1)

					# If the due date is more than 1 hour into the future, send a goodluck email
					if exam.due_date > after_1_hour:
						send_goodluck_email_task.apply_async(
							args=[
								user.email
							],

							# Send one hour before exam
							eta=hour_before_due
						)
				
				print(f"{user.is_subbed=}")

				return Response(status=status.HTTP_201_CREATED)
			return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	raise Http404

@api_view(["POST"])
def unsubscripe_view(request):
	if request.is_ajax() and request.method == "POST":
		data = {
			"email": request.data.get("email", None),
		}

		try:
			user = models.User.objects.get(email=data["email"])
			
			# Exception when user isn't subbed
			assert user.is_subbed == True
			user.is_subbed = False
			user.save()

			return Response(status=status.HTTP_200_OK)

		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	raise Http404