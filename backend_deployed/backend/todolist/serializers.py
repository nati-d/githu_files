from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Todo
        fields = ['id', 'task', 'completed', 'created', 'updated']
        
class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TestModel
        fields = ['name']       
        
        
        