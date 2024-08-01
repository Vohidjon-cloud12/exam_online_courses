from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField

from courses.models import CourseComment, ContactMessage, User


class CourseCommentForm(forms.ModelForm):
    class Meta:
        model = CourseComment
        fields = ['name', 'email', 'comment', 'rating']


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'subject']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email doesn't exist")
        return email

    def clean_password(self):
        password = self.data.get('password')
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise forms.ValidationError(" Password doesn't match")
        except User.DoesNotExist:
            raise forms.ValidationError("Email or Password doesn't match")
        return password


class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
