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
from courses.views.basic_info import BasicInfo
from courses.views.contact_direction import ContactDirection
from courses.views.comments import Comments
from courses.views.summary import Summary
from courses.views.users_view import UsersView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BasicInfo.as_view(), name="login"),
    path('contact_direction/', ContactDirection.as_view(), name="contact_direction"),
    path('comments/', Comments.as_view(), name="comments"),
    path('summary/', Summary.as_view(), name="summary"),
    path('users_view/', UsersView.as_view(), name="users_view"),
]
