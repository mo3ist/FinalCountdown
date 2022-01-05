from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.utils.log import get_task_logger

from accounts import emails

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
app = Celery('conf')

logger = get_task_logger(__name__)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, send_periodic_emails_task.s(), name='send emails every 1 min')

@app.task(name="send_initial_email_task")
def send_initial_email_task(email, due_date):
    emails.send_initial_email(email, due_date)
    logger.info(f"INITIAL: An email was sent to'{email}'.")
    return True

@app.task(name="send_goodluck_email_task")
def send_goodluck_email_task(email):
    emails.send_goodluck_email(email)
    logger.info(f"GOODLUCK: An email was sent to'{email}'.")
    return True

@app.task(name="send_periodic_emails_task")
def send_periodic_emails_task():
    emails.send_periodic_emails()
    logger.info(f"PERIODIC: Emails were sent to users")
    return True