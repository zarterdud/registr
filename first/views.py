# from typing import Any
# from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile
# from .forms import RegisterUserForm


# def login(request):
#     return render(request, 'templates/login.html')


def registr(request):
    return HttpResponse("<h1>Регистрация завершена</h1>")


# class WomenHome(ListView):
#     model = registr
#     template_name = '''
#     <!DOCTYPE html>
# <html>
# <head>
#   <title>Регистрация</title>
# </head>
# <body>
#   <h2>Регистрация</h2>
#   <form method="POST" action="/register">
#     <label for="username">Имя пользователя:</label>
#     <input type="text" id="username" name="username"><br><br>

#     <label for="password">Пароль:</label>
#     <input type="password" id="password" name="password"><br><br>

#     <input type="submit" value="Зарегистрироваться">
#   </form>
# </body>
# </html>
# '''
#     context_object_name = 'posts'

#     #     context['menu'] = menu
#     #     context['title'] = 'Главная страница'
#     #     context['cat_selected'] = 0
#     #     return context


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "templates/registration.html"
    success_url = reverse_lazy("templates:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        user = authenticate(
            self.request,
            username=username,
            password1=password1,
            password2=password2
        )
        login(request=self.request, user=user)
        return response
