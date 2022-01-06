from django.template.loader import render_to_string 
from django.core.mail import EmailMessage
from django.conf import settings 
from django.contrib.auth import get_user_model
from django.core import mail
from django.utils import timezone
from django.db.models import Q

def send_initial_email(email):
	
	from core import models as core_models # bad practice, but a quick fix for a celery error. move tasks to a separate folder.
	
	exams = core_models.Exam.objects.all()
	
	context={
		"exams": [x.name for x in exams],
		"unsub_url": "https://www.youtube.com/"
	}

	html_body = render_to_string("initial_email.html", context=context)
	email = EmailMessage(
		"The end is near ⏳",
		html_body,
		settings.EMAIL_HOST_USER,
		[email, ]
	)
	email.content_subtype = 'html'

	return email.send(fail_silently=False)

def send_goodluck_email(email):
	User = get_user_model()

	try:
		user = User.objects.get(email=email)
	except:
		return

	# If still subbed
	if not user.is_admin and user.is_subbed:
		context={
			"unsub_url": "https://www.youtube.com/"
		}
		html_body = render_to_string("goodluck_email.html", context=context)

		email = EmailMessage(
			'The end is here ⌛',
			html_body,
			settings.EMAIL_HOST_USER,
			[email, ]
		)
		email.content_subtype = 'html'

	return email.send(fail_silently=False)


def send_periodic_emails():
	User = get_user_model()
	connection = mail.get_connection()
	connection.open()

	emails = []

	# sorted by due_date
	from core import models as core_models # bad practice, but a quick fix for a celery error. move tasks to a separate folder.

	last_due_exam = core_models.Exam.objects.all().first()

	for user in User.objects.all():
		after_1_hour = timezone.now() + timezone.timedelta(minutes=1)

		# Activities that has NOT been sent to user
		activities = core_models.Activity.objects.filter(
			~Q(users=user)	# Django is smart enough to match "user" in M2M 
		)

		# send if it's more that 1 hours into the future
		# Don't send if
		# - User is admin
		# - User isn't subbed
		# - Due in less than 'after_1_hour'
		# - No activities left
		if not user.is_admin and user.is_subbed and last_due_exam.due_date > after_1_hour and activities:
			timedelta = last_due_exam.due_date - timezone.now()
			
			activity = activities.first()

			# Add user not to send the activity again
			activity.users.add(user)

			context = {
				"name": last_due_exam.name,
				"countdown": str(timedelta),
				"activity": activity.text,
				"unsub_url": "https://www.youtube.com"
			}
			html_body = render_to_string("periodic_email.html", context=context)
			email = mail.EmailMessage(
				f'فاضل {str(timedelta)} 🙂',
				html_body,
				settings.EMAIL_HOST_USER,
				[user.email],
			)
			email.content_subtype = 'html'
			emails.append(email)

	if emails:
		connection.send_messages(emails)

	connection.close()
	return True