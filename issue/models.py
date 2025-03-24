from django.db import models


# Create your models here.

class Issues(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField(blank=True,null=True)
    progress_details = models.TextField(blank=True,null=True)
    date_of_update = models.DateField(auto_now=True)
    deadline = models.DateField(blank=True,null=True)
    type = models.IntegerField(choices=[(0,"不具合"),(1,"タスク"),(2,"要望"),(3,"その他")])
    person = models.IntegerField(choices=[(0,"担当A"),(1,"担当B"),(2,"担当C"),(3,"担当D")])
    progress = models.IntegerField(choices=[(0,"完了"),(1,"進行中"),(2,"未対応"),(3,"保留"),(4,"対応不要")])
    budget = models.IntegerField(blank=True,null=True)

