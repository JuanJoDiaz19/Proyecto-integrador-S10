from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View


class ContactDirection(View):
    
    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request):
        print("me cago en la putaaaa")
        print(request.POST)
        direction = request.POST.get('direction')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        
        request.session['direction'] = direction
        request.session['phone_number'] = phone
        request.session['email'] = email

        return redirect ('/comments')