from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from users.models import User


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(FormStyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', )

    def __init__(self, *args, **kwargs):
        """Скрывает password при заполнении"""
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserRegisterForm(FormStyleMixin, UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )
