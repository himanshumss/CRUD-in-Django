from django.shortcuts import render

# Create your views here.
from create_app.models import student
def readData(request):
    stud = student.objects.all()
    return render(request, 'readData.html', {'stud': stud})