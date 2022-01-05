from rest_framework import serializers
from rest_framework import exceptions

from accounts import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = "__all__"

	password = serializers.CharField(required=False)