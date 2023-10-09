from django.forms import ModelForm
from courses.models import Course, Professor, User

class CreateUser(ModelForm):
    class Meta:
        model = User
        fields = ['name','last_name']