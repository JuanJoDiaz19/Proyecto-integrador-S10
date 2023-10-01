from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from courses.forms.create_course_form import CreateCourseForm
from courses.models import Course, Professor
from courses.util.query_util import get_professor_by_id


class CoursesCreate(View):
    def get(self, request):
        professorID = request.session.get('professor', -1)
        try:
            professor = get_professor_by_id(professorID)
            return render(request, 'courses_create.html', {
                'form':CreateCourseForm,
                'professor':professor
            })
        except Professor.DoesNotExist:
            return render(request, 'courses_create.html', {
                'form':CreateCourseForm
            })
        
        
    def post(self, request):
        print(request.POST)
        name = request.POST['name']
        faculty = request.POST['faculty']
        description = request.POST['description']    
        professorFK = request.POST['professor']  
        professor = get_professor_by_id(professorFK)
        course = Course(name=name, faculty=faculty, description=description, professor= professor)
        course.save()

        del request.session['professor']

        return redirect("/")
    
    