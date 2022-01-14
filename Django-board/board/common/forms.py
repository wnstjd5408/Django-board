from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호확인', widget=forms.PasswordInput)
    # name = forms.CharField(label="성함")
    # date_of_birth = forms.DateField(label="생년월일")
    # gender = forms.CharField(label="성별")

    class Meta:
        model = User
        fields = ['email', 'name', 'date_of_birth', 'gender']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("비밀번호가 맞지 않습니다")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.name = self.cleaned_data.get("name")
        # user.date_of_birth = self.cleaned_data.get("date_of_birth")
        # user.gender = self.cleaned_data.get("gender")
        if commit:
            user.save()
        return user

    def clean(self):

        cleaned_data = super().clean()

        email = cleaned_data.get('email', '')
        password1 = cleaned_data.get('password1', '')
        password2 = cleaned_data.get('password2', '')
        name = cleaned_data.get('name', '')
        date_of_birth = cleaned_data.get('date_of_birth', '')
        gender = cleaned_data.get('gender', '')

        if email == '':
            return self.add_error('email', '를 입력해 주세요!!')
        elif 8 > len(password1):
            return self.add_error('password1', '비밀번호는 8자리 이상을 적어주세요.')
        else:
            self.email = email
            self.password1 = password1
            self.password2 = password2
            self.name = name
            self.date_of_birth = date_of_birth
            self.gender = gender


class CustomUserChangoForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'date_of_birth', 'gender')


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'date_of_birth', 'gender',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
