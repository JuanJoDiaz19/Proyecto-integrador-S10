from django.forms import ModelForm
from courses.models import Course, Professor

class NameAndLastName(ModelForm):
    class Meta:
        model = Course
        fields = ['name','faculty', 'description']