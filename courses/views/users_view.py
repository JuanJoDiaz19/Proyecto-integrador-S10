from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.models import User


class UsersView(View):
    
    def get(self, request):
        users= User.objects.all()
        return render(request, 'users_view.html', {'users':  users})
    