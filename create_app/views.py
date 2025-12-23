from django.shortcuts import render
from create_app.models import student
# Create your views here.
def createdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll_no')
        course = request.POST.get('course')
        mobile = request.POST.get('mobile')
        stu = student(name=name, roll=roll, course=course, mobile=mobile)
        stu.save()
        return render(request, 'createData.html', {'msg': 'Data Created Successfully'})
    return render(request, 'createData.html')

def home(request):
    return render(request, 'dashboard.html')