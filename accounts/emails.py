from django.core.mail import EmailMessage
from django.conf import settings 
from django.contrib.auth import get_user_model
from django.core import mail
from django.utils import timezone

def send_initial_email(email, due_date):
	
	context = {
		'email': email,
		'capsule_creation_date': due_date,
	}

	email_subject = 'The end is nearer'
	# email_body = render_to_string('email_template.txt', context)
	email_body = "HAHAHA"
	email = EmailMessage(
		email_subject,
		email_body,
		settings.EMAIL_HOST_USER,
		[email, ]
	)

	return email.send(fail_silently=False)

def send_goodluck_email(email):
	context = {
		'email': email,
		# 'capsule_creation_date': due_date,
	}

	email_subject = 'The end is here'
	email_body = "HAHAHA"
	email = EmailMessage(
		email_subject,
		email_body,
		settings.EMAIL_HOST_USER,
		[email, ]
	)

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

		# send if it's more that 1 hours into the future
		if not user.is_admin and user.is_subbed and last_due_exam.due_date > after_1_hour:
			email = mail.EmailMessage(
				'Periodic Test',
				'Done',
				settings.EMAIL_HOST_USER,
				[user.email],
			)
			emails.append(email)

	if emails:
		connection.send_messages(emails)

	connection.close()
	return True