from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View


class Comments(View):
    
    def get(self, request):
        return render(request, 'comments.html')
    
    def post(self, request):
        comment = request.POST.get('comment')
        request.session['comment'] = comment

        return redirect('/summary')
       