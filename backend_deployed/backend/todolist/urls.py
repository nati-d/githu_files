from django.contrib import admin
from .views import TestModelListCreate, TestModelRetrieveUpdateDestroy, TodoListCreate, TodoRetrieveUpdateDestroy
from django.urls import path,include

urlpatterns = [
  path('api/todos/', TodoListCreate.as_view(), name='todo-list-create'),
  path('api/todos/<int:pk>/', TodoRetrieveUpdateDestroy.as_view(), name='todo-detail'),
  path('api/testmodel/', TestModelListCreate.as_view(), name='testmodel-list-create'),
  path('api/testmodel/<int:pk>/', TestModelRetrieveUpdateDestroy.as_view(), name='testmodel-detail'),
]
