from django.forms import ModelForm ,CharField,PasswordInput
from django.contrib.auth.models import User

class SingeUPForm(ModelForm):
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']