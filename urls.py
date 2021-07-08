from django.urls import path

from .views import home, add_todo, update_todo, delete_todo, todo_completed

urlpatterns = [
    path("", home, name="todo_home"),
    path("add_todo", add_todo, name="todo_add"),
    path("update_todo", update_todo, name="update_todo"),
    path("delete", delete_todo, name="delete_todo"),
    path("todo_completed", todo_completed, name="todo_completed"),
]

#  http://127.0.0.1:8000/todo/delete?todo_id=7
