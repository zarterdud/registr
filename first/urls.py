# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'first'

urlpatterns = [
    path('', views.registr),
    path("register/", views.RegisterView.as_view()),
    path('login/', views.login, name='login'),
]


# class DataMixin:
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         cats = Category.objects.all()
#         context['menu'] = menu
#         context['cats'] = cats
#         if 'cats_selected' not in context:
#             context['cat_selected'] = 0
#         return context
