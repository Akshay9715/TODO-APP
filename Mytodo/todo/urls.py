from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('create/todo/',views.create_todo,name='create_todo'),
    path('complete_todo/<int:todo_id>', views.complete_todo,name='complete_todo'),
    path('delete/todo<int:todo_id>',views.delete_todo,name='delete_todo'),
]