from django.views.generic import CreateView
from users.models import User
from users.forms import UserRegisterForm


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = '/users/login/'
