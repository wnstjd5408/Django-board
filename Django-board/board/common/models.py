from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, name, gender, date_of_birth, password=None):
        if not email:
            raise ValueError('must have user email address')

        user = self.model(
            email=self.normalize_email(email),
            # self.normalize_email? - >email을 정규화
            # -> @ 뒤에 값을 대소문자 구분 x로 만듦으로서 다중 가입 방지
            name=name,
            gender=gender,
            date_of_birth=date_of_birth,
        )
        # password hash 및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,  gender, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
            gender=gender,
            date_of_birth=date_of_birth,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    Gender_choices = {
        ('남', '남자'),
        ('여', '여자')
    }
    name = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=Gender_choices)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'gender']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
