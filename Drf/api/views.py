from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
import pdb

# create your views here

class GetAllEmployees(APIView):

	def get(self,request,format=None):
		
			try:
				employees=Employee.objects.all()
				serializer=EmployeeSerializer(employees,many=True)
				return Response(serializer.data)

			except Employee.DoesNotExist:
				raise Http404

	
class InsertEmployee(APIView):

	def post(self,request,format=None):
			try:
				serializer=EmployeeSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data,status=status.HTTP_201_CREATED)
			except Employee.DoesNotExist:
					raise Http404
				

class UpdateEmployee(APIView):

	def get_object(self,Employee_Id):
			try:
				return Employee.objects.get(pk=Employee_Id)
			except Employee.DoesNotExist:
				raise Http404 
	def put(self,request,Employee_Id,format=None):

			try:
				employee=self.get_object(Employee_Id)
				serializer=EmployeeSerializer(employee,data=request.data)
				pdb.set_trace()
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data,status=status.HTTP_201_CREATED)
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			except Employee.DoesNotExist:
					raise Http404

class DeleteEmployee(APIView):
	def delete(self,request,Employee_Id,format=None):

			try:
				employee=UpdateEmployee.get_object(self,Employee_Id)
				employee.delete()
				return Response(status=status.HTTP_204_NO_CONTENT)
			except Employee.DoesNotExist:
					raise Http404

