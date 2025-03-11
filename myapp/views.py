from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost,Employee
from .serializers import BlogPostSerializer,EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends=[SearchFilter]                     #search filter 
    search_fields=['title']

    def delete(self,request,*args,**kwargs):
        BlogPost.objects.all().delete
    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    

# Use the filter class in the API view
from myapp.filter import EmployeeFilter
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]         #custom filter
    filterset_class = EmployeeFilter
    ordering_fields=['salary']


    def delete(self,request,*args,**kwargs):
        Employee.objects.all().delete

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

