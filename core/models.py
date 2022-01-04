from django.db import models

class Exam(models.Model):
	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()

	def __str__(self):
		return self.name

class Activity(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text[:25]