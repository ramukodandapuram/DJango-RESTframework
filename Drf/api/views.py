from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
import pdb

# create your views here

# Get Record By ID(primary key)
class EmployeeDetailsByID(APIView):
	
	def get_object(self,pk):
		try:
			return Employee.objects.get(pk=pk)
		except Employee.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		employee=self.get_object(pk)
		serializer=EmployeeSerializer(employee)
		return Response(serializer.data)

# Get all records present in requested database

class EmployeesDetails(APIView):

	def get(self,request,format=None):
		employee=Employee.objects.all()
		serializer=EmployeeSerializer(employee,many=True)
		return Response(serializer.data)

# Inserting new record into the database

class InsertEmployee(APIView):
	def post(self,request,format=None):
		try:
			
			serializer=EmployeeSerializer(data=request.data)
			
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
		except Employee.DoesNotExist:
			raise Http404

# Updating record based on ID (key)

class UpdateEmployee(APIView):

	def put(self,request,pk,format=None):
		try:
			employee=EmployeeDetailsByID.get_object(self,pk)
			
			data=(EmployeeSerializer(employee).data)
			requested_data=request.data
			data.update(requested_data)
			serializer=EmployeeSerializer(employee,data=data)
			
			if serializer.is_valid():
				serializer.save()
				return Response(data,status=status.HTTP_201_CREATED)

			
		except Employee.DoesNotExist:
			raise Http404
# Deleting  record based on ID(key)

class DeleteEmployee(APIView):

	def delete(self,request,pk,format=None):

		try:
			employee=EmployeeDetailsByID.get_object(self,pk)
			employee.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
			

		except Employee.DoesNotExist:
			raise Http404



