from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee

from .serializers import employeeSerializer

# Create your views here.


class EmployeeList(APIView):

    def get(self,request):
        employee=Employee.objects.all()
        serializer=employeeSerializer(employee,many=True)
        return Response(serializer.data)

    def post(self):
        pass