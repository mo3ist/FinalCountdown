from django.core.mail import EmailMessage
# from django.template import Context
# from django.template.loader import render_to_string
from django.conf import settings 

def send_email(email, due_date):
	
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