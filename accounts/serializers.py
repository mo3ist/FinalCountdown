from rest_framework import serializers
from rest_framework import exceptions

from accounts import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = "__all__"

	password = serializers.CharField(required=False)

	def create(self, validated_data):
		user = models.User(email=validated_data["email"])
		user.set_password("")
		user.save()
		return user