from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Нет пользователя с таким именем")
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
            if not user.is_active:
                raise forms.ValidationError("Пользователь больше не активен")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Введите пароль ещё раз', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password















