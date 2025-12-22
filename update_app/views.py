from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from create_app.models import student

def updateData(request, roll):
    stu = get_object_or_404(student, roll=roll)

    if request.method == "POST":
        stu.name = request.POST.get("name")
        stu.course = request.POST.get("course")
        stu.mobile = request.POST.get("mobile")
        stu.save()

        return redirect("read_data")

    return render(request, "updateData.html", {"stu": stu})




#----------------------Update Student with Dropdown----------------------#
# views.py
from django.shortcuts import render, redirect
from create_app.models import student

def updateStudent(request):
    students = student.objects.all().order_by("name")
    selected_student = None

    # Step 1: Student selected from dropdown
    if request.method == "POST" and "select_student" in request.POST:
        roll = request.POST.get("roll")
        selected_student = student.objects.get(roll=roll)

    # Step 2: Update student data
    elif request.method == "POST" and "update_student" in request.POST:
        roll = request.POST.get("roll")
        selected_student = student.objects.get(roll=roll)

        selected_student.name = request.POST.get("name")
        selected_student.course = request.POST.get("course")
        selected_student.mobile = request.POST.get("mobile")
        selected_student.save()

        return redirect("update_student")

    return render(request, "updateStudent.html", {
        "students": students,
        "stu": selected_student
    })
