from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
# Register your models here.
    list_display = ('email', 'name', 'date_of_birth', 'gender', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'date_of_birth', 'gender', 'password1', 'password2')}
         ),
    )
    search_fields = ('name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
