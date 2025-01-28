import random
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from users.models import User
from users.forms import UserRegisterForm


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy('dogs:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create user'
        return context

    def form_valid(self, form):
        user = form.save()
        user.is_active = True

        current_site = self.request.get_host()
        subjet = 'Подтверждение регистрации'

        verification_code = ''.join(str(random.randint(0, 9)) for _ in range(8))
        user.verification_code = verification_code

        message = (f'Вы успешно зарегистрировались на нашем сайте. Чтобы продолжиться пользоваться сайтом, перейде по'
                   f'ссылке http://{current_site}/users/confirm/ и введите свой код верификации {verification_code}')

        user.save()

        print(message)
        return super().form_valid(form)


class ConfirmRegisterView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/confirm_registration.html')

    def post(self, request, *args, **kwargs):
        verification_code = request.POST.get('verification_code')
        user = get_object_or_404(User, verification_code=verification_code)

        if user:
            user.is_active = True
            user.save()
            return redirect('users:login')
        return redirect('dogs:index')
