from .models import Employee
from rest_framework import serializers



class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields=('Employee_Id','Employee_Name','Department_Name')