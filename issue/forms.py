import os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProgressComment, Issues


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
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


""" 検索フォーム """
class SearchForm(forms.Form):
    # 期限（from）
    from_deadline = forms.DateField(
        label='期限（from）',
        required=False,
        widget=DataInput(),# カレンダー
    )

    # 期限（to）
    to_deadline = forms.DateField(
        label='期限（to）',
        required=False,
        widget=DataInput(),# カレンダー
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
    TYPE_CHOICES = [('', '---------')] + list(Issues._meta.get_field('type').choices)
    # タイプ
    type = forms.ChoiceField(
        label='タイプ',
        required=False,
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )
    # 担当者
    person = forms.ModelChoiceField(
        label='担当者',
        required=False,
        queryset=User.objects.filter(is_superuser=False),
        widget=forms.Select(attrs={'class': 'form'})
    )

    # モデルからフィールドを引っぱってきてリスト作成
    PROGRESS_CHOICES = [('', '---------')] + list(Issues._meta.get_field('progress').choices)
    # 進捗状況
    progress = forms.ChoiceField(
        label='進捗状況',
        required=False,
        choices=PROGRESS_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )


""" 添付ファイル アップロードフォーム """
# 複数のファイルをアップロードするウィジェットクラス
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


# 複数のファイルをアップロードするフィールドクラス
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


# 複数のファイルをアップロードするフォームクラス
class FileFieldForm(forms.Form):
    #  複数のファイルをアップロードするフィールドを作成
    files = MultipleFileField(label="Ctrl キーで複数のファイルを選択できます。")

    # 拡張子を限定する
    def clean_files(self):
        files = self.cleaned_data["files"]
        for file in files:
            extension = os.path.splitext(file.name)[1]

            # 拡張子
            if not extension.lower() in [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".webp", ".png", ".jpg", ".jpeg"]:
                raise forms.ValidationError("アップロード可能なファイルを選択してください")
        return files