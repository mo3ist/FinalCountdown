from django.shortcuts import render

from core import serializers
from core import models

def home_view(request):

	exam_queryset = models.Exam.objects.all()
	exam_serializer = serializers.ExamSerializer(exam_queryset, many=True)
	context = {"exams": exam_serializer.data}

	return render(request, 'home.html', context)