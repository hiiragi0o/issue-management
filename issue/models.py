from django.db import models

# Create your models here.

class Issues(models.Model):
    title = models.CharField(max_length=50)
    record = models.TextField(blank=True,null=True)
    type = models.IntegerField(choices=[(0,"不具合"),(1,"タスク"),(2,"要望"),(3,"その他")])
    amount = models.IntegerField()
    date = models.DateField()
