from django.db import models

class Exam(models.Model):
	
	class Meta:
		ordering = ('-due_date',)

	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()
	image = models.ImageField(upload_to="core")

	def __str__(self):
		return self.name

class Activity(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text[:25]