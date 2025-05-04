from django.contrib import admin
from .models import Issues, ProgressComment, Document

# models.pyで書いたclassをregister＝登録する

admin.site.register(Issues)
admin.site.register(ProgressComment)
admin.site.register(Document)