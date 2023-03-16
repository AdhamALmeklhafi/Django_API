from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path("<int:pk>/", ListTodo.as_view(), name="todo_detail"),
    path("", ListTodo.as_view(), name="todo_list"),
]
