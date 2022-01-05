from django.core.mail import EmailMessage
from django.conf import settings 
from django.contrib.auth import get_user_model
from django.core import mail

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

def send_periodic_emails():
	User = get_user_model()
	connection = mail.get_connection()
	connection.open()

	emails = []
	for user in User.objects.all():
		if not user.is_admin:
			email = mail.EmailMessage(
				'Periodic Test',
				'Done',
				settings.EMAIL_HOST_USER,
				[user.email],
				# connection=connection
			)
			emails.append(email)
	connection.send_messages(emails)

	connection.close()
	return True