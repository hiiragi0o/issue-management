from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issues(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField(blank=True,null=True)
    create_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True,null=True)
    type = models.IntegerField(choices=[(0,"不具合"),(1,"タスク"),(2,"要望"),(3,"その他")])
    person =  models.ForeignKey(User, related_name='person_user',  on_delete=models.PROTECT, limit_choices_to={"is_superuser":False})# 担当者
    # user との名前の競合を解消するため related_name= を追加
    progress = models.IntegerField(choices=[(0,"完了"),(1,"進行中"),(2,"未対応"),(3,"保留"),(4,"対応不要")])
    budget = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)# 作成者=loginユーザー

# self がRecord というclassから作成された object 
# そのtitleを返す
    def __str__(self):
        return self.title
    
# 記事に紐づくコメント
class ProgressComment(models.Model):
    comment = models.TextField() # 必須入力
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={"is_superuser":False})
    issues = models.ForeignKey(Issues, on_delete=models.CASCADE)# 対象課題

    class Meta:
        ordering = ['-create_date']  # デフォルトで'create_date'で降順に並び替え
    
    def __str__(self):
        return self.comment


# 記事に紐づく添付ファイル
class UploadFile(models.Model):
    title = models.CharField('ファイル名',max_length=50)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='uploaded_files')# 対象課題

    def __str__(self):
        return self.title

    # ファイル名を取得
    @property
    def filename(self):
        return self.file.name.split("/")[-1]  # uploads/を除くファイル名だけ取得

    # ファイルサイズを取得
    def get_file_size(self):
        return self.file.size # バイト単位のみ