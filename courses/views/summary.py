from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.models import User


class Summary(View):
    
    def get(self, request):
        name =  request.session.get('name', -1)
        last_name =  request.session.get('last_name', -1)
        direction =  request.session.get('direction', -1)
        phone =  request.session.get('phone_number', -1)
        email =  request.session.get('email', -1)
        comment =  request.session.get('comment', -1)

        

        return render(request, 'summary.html', 
                      {'name': name, 'last_name': last_name, 'direction': direction, 'phone': phone, 'email': email, 'comment': comment } )
    
    def post(self, request):

        user_name =  request.POST.get('name')
        user_last_name =  request.POST.get('last_name')
        user_direction =  request.POST.get('direction')
        user_phone =  request.POST.get('phone_number')
        user_email =  request.POST.get('email')
        user_comment =  request.POST.get('comment')

        User.objects.create(
            name=user_name,
            last_name= user_last_name,
            address= user_direction,
            phone_number=user_phone,
            email=user_email,
            comment=user_comment,
        )

        return redirect('/users_view/')
       