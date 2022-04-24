from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate


# User = settings.AUTH_USER_MODEL
User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'confirm_password'
        )

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('The passwords do not match.')

        return super(UserRegisterForm, self).clean()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This user doesn\'t exist.')

            if not user.check_password(password):
                raise forms.ValidationError('Please check your credentials.')

            if not user.is_active:
                raise forms.ValidationError('Please active your account.')

        return super(UserLoginForm, self).clean()
