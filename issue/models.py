from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issues(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField(blank=True,null=True)
    create_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True,null=True)
    type = models.IntegerField(choices=[(0,"不具合"),(1,"タスク"),(2,"要望"),(3,"その他")])
    person =  models.ForeignKey(User, related_name='person_user',  on_delete=models.PROTECT)
    # user との名前の競合を解消するため related_name= を追加
    progress = models.IntegerField(choices=[(0,"完了"),(1,"進行中"),(2,"未対応"),(3,"保留"),(4,"対応不要")])
    budget = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)

# self がRecord というclassから作成された object 
# そのtitleを返す
    def __str__(self):
        return self.title
    
class ProgressComment(models.Model):
    comment = models.TextField() # 必須入力
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    issues = models.ForeignKey(Issues, on_delete=models.PROTECT)


    