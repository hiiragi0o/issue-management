from django.contrib import admin
from .models import Issues,ProgressComment

# models.pyで書いたIssueをregister＝登録する

admin.site.register(Issues)
admin.site.register(ProgressComment)