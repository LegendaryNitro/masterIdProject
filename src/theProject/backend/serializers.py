from rest_framework import serializers
from .models import *

class RegistererSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registers
		fields ='__all__'


class ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = ApplicationForm
		fields ='__all__'