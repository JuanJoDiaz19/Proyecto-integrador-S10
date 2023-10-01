"""
URL configuration for p1sisworkshop project.

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
from courses.views.professor_list import ProfessorList
from courses.views.professor_create import ProfessorCreate
from courses.views.courses_create import CoursesCreate
from courses.views.courses_main import CoursesMain
from courses.views.signin import Signin
from courses.views.signup import Signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CoursesMain.as_view(), name="courses"),
    path('createcourse/', CoursesCreate.as_view(), name="createcourse"),
    path('createprofessor/', ProfessorCreate.as_view(), name="createprofessor"),
    path('signup/', Signup.as_view(), name="signup"),
    path('signin/', Signin.as_view(), name="signin"),
    path('signout/', CoursesMain.signout, name="signout"),
    path('chooseprofessor/', ProfessorList.as_view(), name="chooseprofessor"),
]
