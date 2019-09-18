from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoView, name="todoView"),
    path('addTodo/', views.addTodo, name="addTodo"),
    path('deleteitem/<int:todo_id>/', views.deleteitem, name="deleteitem")

]
