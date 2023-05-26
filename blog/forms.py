from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('DF', 'Draft'),
    ('PB', 'Published'),
)
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Parol',widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Parolni takrorlang',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password_2']

    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError("Ikkala parolingiz bir xil bo'lishi kerak! ")
        return data['password_2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class PostAddForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model=Post
        fields = ['title','author','body','slug','status']