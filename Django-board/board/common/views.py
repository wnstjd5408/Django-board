from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'common/join.html'
    success_url = reverse_lazy('common:login')


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'common/update.html'
    success_url = '/'

    def get_object(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user


class UserDetailView(DetailView):
    model = User
    template_name = 'common/info.html'


class UserDeleteView(DeleteView):
    form_class = CheckPasswordForm
    model = User
    context_object_name = 'user'
    template_name = 'common/delete.html'
    success_url = '/'


class UserPasswordChangeview(PasswordChangeView):

    template_name = 'common/password_change.html'
    success_message = 'Password changed'
    success_url = reverse_lazy('bo:index')

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     form.fields["old_password"].widget.attrs = {
    #         "placeholder": "현재 비밀번호"}
    #     form.error_messages["password_mismatch"] = "비밀번호가 일치하지 않습니다."
    #     form.fields["new_password1"].widget.attrs = {
    #         "placeholder": "새로운 비밀번호"}
    #     form.fields["new_password2"].widget.attrs = {
    #         "placeholder": "비밀번호 확인"
    #     }
    #     return form

    # def get_success_url(self):
    #     return self.request.user.get_absolute_url()
