from django.shortcuts import render, redirect

from .models import Note


def home(request):
    queryset_note = Note.objects.filter(completed=False)
    print("Count => ", Note.objects.filter(completed=True).count())
    return render(request, "ui_add_todo.html", context={'queryset_note': queryset_note})


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        print(title, description)
        obj_note = Note(title=title, description=description)
        obj_note.save()

    return redirect("todo_home")


def update_todo(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        title = request.POST.get("title")
        description = request.POST.get("description")

        obj_note = Note.objects.get(id=todo_id)
        obj_note.title = title
        obj_note.description = description
        obj_note.save()

        return redirect("todo_home")

    todo_id = request.GET.get("todo_id")
    obj_todo = Note.objects.get(id=todo_id)
    return render(request, "add_todo.html", context={'obj_todo': obj_todo})


def delete_todo(request):
    if request.method == "GET":
        todo_id = request.GET.get("todo_id")
        obj_todo = Note.objects.get(id=todo_id)
        obj_todo.delete()

    return redirect("todo_home")

# http://127.0.0.1:8000/todo/todo_completed?todo_id=821
# http://127.0.0.1:8000/todo/todo_completed


def todo_completed(request):
    if request.method == "GET":
        todo_id = request.GET.get("todo_id")
        if Note.objects.filter(id=todo_id):     # [] -> [obj]
            obj_todo = Note.objects.get(id=todo_id)
            obj_todo.completed = True
            obj_todo.save()
        else:
            print(f"Record with id {todo_id} does not exist!")

    return redirect("todo_home")
