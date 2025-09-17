from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET", "POST"])
def stu_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT","PATCH","DELETE"])
def stu_detail(request,pk):
    if pk:

        if request.method == 'GET':
            snippet = request.get_object(pk)
            serializer = StudentSerializer(snippet)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            snippet = request.get_object(pk)
            serializer = StudentSerializer(snippet, data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'PATCH':
            snippet = request.get_object(pk)
            serializer = StudentSerializer(snippet, data=request.data , partial=True)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            snippet = request.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    

    
