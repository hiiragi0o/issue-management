from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )

# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User