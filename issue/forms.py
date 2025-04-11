from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProgressComment


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )

# ログインフォームを追加
class LoginForm(AuthenticationForm):
    class Meta:
        model = User

# コメント投稿フォーム
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = ProgressComment
        fields = ('comment',)