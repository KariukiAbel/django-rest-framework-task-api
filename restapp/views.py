from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task
from rest_framework import filters

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers
    
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    # define filtering field
    filter_fields = ('completed',)
    ordering = ('-date_created',)
    
    
'''class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers
    
class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers
    '''