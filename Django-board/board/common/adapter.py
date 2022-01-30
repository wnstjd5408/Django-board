from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        data = form.cleaned_data
        user.name = data.get('name')
        user.date_of_birth = data.get('date_of_birth')
        user.gender = data.get('gender')
        user.save()
        return user
