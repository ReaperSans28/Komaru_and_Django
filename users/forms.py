from users.models import User
from django.contrib.auth.forms import UserCreationForm
from config.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
