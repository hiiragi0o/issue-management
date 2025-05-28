from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Issues(models.Model):
    title = models.CharField(max_length=50, verbose_name="タイトル")
    contents = models.TextField(blank=True,null=True, verbose_name="内容")
    create_date = models.DateField(auto_now_add=True, verbose_name="作成日")
    deadline = models.DateField(blank=True,null=True, verbose_name="期限日")
    type = models.IntegerField(choices=[(0,"不具合"),(1,"タスク"),(2,"要望"),(3,"その他")], verbose_name="タイプ") # タイプは必須入力
    person =  models.ForeignKey(User, related_name='person_user',  on_delete=models.PROTECT, limit_choices_to={"is_superuser":False}, verbose_name="担当者") 
    # user との名前の競合を解消するため related_name= を追加
    progress = models.IntegerField(choices=[(0,"完了"),(1,"進行中"),(2,"未対応"),(3,"保留"),(4,"対応不要")], verbose_name="進捗状況")
    budget = models.IntegerField(blank=True,null=True, verbose_name="予算")
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT, verbose_name="作成者/loginユーザー")

    class Meta:
        verbose_name = "課題"
        verbose_name_plural = "課題一覧"

    # titleを返す
    def __str__(self):
        return self.title


# 記事に紐づくコメント
class ProgressComment(models.Model):
    comment = models.TextField(verbose_name="コメント") # 必須入力
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")
    user = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={"is_superuser":False}, verbose_name="作成者/loginユーザー")
    issues = models.ForeignKey(Issues, on_delete=models.CASCADE, verbose_name="対象課題")

    class Meta:
        verbose_name = "コメント"
        verbose_name_plural = "コメント一覧"
        ordering = ['-create_date']  # デフォルトで'create_date'で降順に並び替え
    
    def __str__(self):
        return self.comment


# 記事に紐づく添付ファイル
class UploadFile(models.Model):
    title = models.CharField(max_length=50, verbose_name="ファイル名")
    file = models.FileField(upload_to='uploads/', verbose_name="ファイル")  # 'uploads/'ディレクトリに保存
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="アップロード日時")
    issue = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='uploaded_files', verbose_name="対象課題")

    class Meta:
        verbose_name = "添付ファイル"
        verbose_name_plural = "添付ファイル一覧"

    def __str__(self):
        return self.title

    # ファイル名を取得
    @property
    def filename(self):
        return self.file.name.split("/")[-1]  # uploads/を除くファイル名だけ取得

    # ファイルサイズを取得
    @property
    def file_size(self):
        return self.file.size // 1024  # KB単位で取得 