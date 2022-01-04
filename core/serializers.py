from rest_framework import serializers

from core import models

class ExamSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Exam
		fields = '__all__'