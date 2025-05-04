from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProgressComment, Issues


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
        )

    # email が空白の時エラーにする
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__( *args, **kwargs)
        self.fields['email'].required = True


# ログインフォームを追加
class LoginForm(AuthenticationForm):
    class Meta:
        model = User


# カレンダーフォームを作成する
class DataInput(forms.DateInput):
    input_type = 'date'

# Issues用フォーム
class IssuesForm(forms.ModelForm):
    class Meta:
        model = Issues
        fields = ('title', 'contents', 'deadline', 'type', 'person', 'progress', 'budget')
        widgets = {
            'deadline': DataInput(),# カレンダー
        }

# コメント投稿フォーム
class CommentForm(forms.ModelForm):
    class Meta:
        model = ProgressComment
        fields = ('comment',)

# 検索フォーム（作成中）
class SearchForm(forms.Form):
    # 年の選択肢を動的に作る 中身
    years = [(year, f'{year}年') for year in reversed(range(2023,2031))]
    years.insert(0, (0, ''))  # 空白の選択を追加
    YEAR_CHOICES = tuple(years)

    # 月の選択肢を動的に作る
    months = [(month, f'{month}月') for month in range(1, 13)]
    months.insert(0, (0, ''))
    MONTH_CHOICES = tuple(months)

    # 年の選択　外側
    year = forms.ChoiceField(
        label='年での絞り込み',
        required=False,
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )

    # 月の選択
    month = forms.ChoiceField(
        label='月での絞り込み',
        required=False,
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )

    # キーワード
    key_word = forms.CharField(
        label='検索キーワード',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form',
                                        'autocomplete': 'off',
                                        'placeholder': 'キーワード',
                                        })
    )

    # モデルからフィールドを引っぱってきてリスト作成
    PROGRESS_CHOICES = [('', '---------')] + list(Issues._meta.get_field('progress').choices)

    # 進捗状況の検索
    progress = forms.ChoiceField(
        label='進捗状況で絞り込み',
        required=False,
        choices=PROGRESS_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )
