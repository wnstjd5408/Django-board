from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from .forms import *
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'common/join.html'
    success_url = reverse_lazy('common:login')


class UserUpdateView(UpdateView):
    form_class = CustomUserChangoForm
    template_name = 'common/update.html'
    success_url = reverse_lazy('common:detail')


class UserDetailView(DetailView):
    model = User
    template_name = 'common/info.html'
