from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Userz
		fields ='__all__'