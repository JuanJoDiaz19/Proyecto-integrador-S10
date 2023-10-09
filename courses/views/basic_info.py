from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View


class BasicInfo(View):
    
    def get(self, request):
        return render(request, 'basic_info.html')
    
    def post(self, request):
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        
        request.session['name']= name
        request.session['last_name']= last_name
        
        return redirect('/contact_direction')