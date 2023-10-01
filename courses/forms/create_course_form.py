from django.forms import ModelForm
from courses.models import Course, Professor

class CreateCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name','faculty', 'description']