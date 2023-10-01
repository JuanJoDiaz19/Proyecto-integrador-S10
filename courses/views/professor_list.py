from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.util.query_util import get_all_professors


class ProfessorList(View):
    
    def get(self, request):
        professors = get_all_professors()
        return render(request, 'professor_list.html', {
            'professors': professors
        })
    
    def post(self, request):
        request.session['professor'] = request.POST['professor']
        return redirect("/createcourse")
    
