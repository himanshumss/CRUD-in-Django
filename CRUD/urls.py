"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from create_app import views as createviews
from read_app import views as readviews
from update_app import views as updateviews
from delete_app import views as deleteviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", createviews.createdata, name="create_data"),
    path("read/", readviews.readData, name="read_data"),
    path("update/<int:roll>/", updateviews.updateData, name="update_data"),
    path("update-student/", updateviews.updateStudent, name="update_student"),
    path("delete-student/", deleteviews.deleteData, name="delete_data"),
]
