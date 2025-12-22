from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from create_app.models import student

def deleteData(request):
    students = student.objects.all().order_by("name")
    message = None

    if request.method == "POST":
        roll = request.POST.get("roll")

        if roll:
            stud = student.objects.get(roll=roll)
            stud.delete()
            message = "Student record deleted successfully."

    return render(request, "deleteData.html", {
        "students": students,
        "message": message
    })
