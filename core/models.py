from django.db import models
from django.conf import settings

class Exam(models.Model):
	
	class Meta:
		ordering = ('-due_date',)

	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()
	image = models.URLField()

	def __str__(self):
		return self.name

class Activity(models.Model):
	text = models.TextField()
	users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="activities")

	def __str__(self):
		return self.text[:25]