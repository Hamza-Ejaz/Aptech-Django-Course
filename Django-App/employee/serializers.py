from django.db.models.base import Model
from rest_framework import serializers
from django.db import models
from .models import Employee  
class Employees(serializers.ModelSerializer):  
    eid = serializers.CharField(max_length=20)  
    ename = serializers.CharField(max_length=100)  
    eemail = serializers.EmailField()  
    econtact = serializers.CharField(max_length=15)  
    class Meta:  
        model = Employee
        fields = ('__all__')