from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'common/join.html'
    success_url = reverse_lazy('common:login')


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangoForm
    template_name = 'common/update.html'
    success_url = '/'

    def get_object(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user


class UserDetailView(DetailView):
    model = User
    template_name = 'common/info.html'
