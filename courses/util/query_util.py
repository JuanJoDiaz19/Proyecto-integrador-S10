from django.db.models import Q
from courses.models import Course, Professor


def get_courses_by_name(query):
    return Course.objects.filter(Q(name__icontains=query) )

def get_courses_by_professor(professor_name):
    return Course.objects.filter(professor__name__icontains=professor_name)

def get_courses_by_faculty(query):
    return Course.objects.filter(Q(faculty__icontains=query) )

def get_courses_by_query(query):
    return Course.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

def get_all_professors():
    return Professor.objects.all()

def get_professor_by_id(query):
    return Professor.objects.get(Q(id=query))