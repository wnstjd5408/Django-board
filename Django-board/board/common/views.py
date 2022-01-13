from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.
from .forms import UserCreationForm


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'common/join.html'
    success_url = "/"
