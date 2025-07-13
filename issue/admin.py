from django.contrib import admin
from import_export.admin import ImportExportModelAdmin # ImportExportModelAdminを継承して、インポート・エクスポート機能を追加
from .models import Issues, ProgressComment, UploadFile


# Issuesモデルにエクスポート機能を追加
@admin.register(Issues) # admin.site.register(Issues) の代わりにデコレータを使用
class IssuesAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('id', 'title', 'type', 'create_date')
    search_fields = ('title', 'contents')  # タイトルと内容の検索を可能にする
    list_filter = ('type', 'progress', 'person')  # タイプ、進捗状況、担当者でのフィルタリングを追加


# ProgressCommentモデルにエクスポート機能を追加
@admin.register(ProgressComment)
class ProgressCommentAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('id', 'comment', 'create_date', 'issues', 'user')
    search_fields = ('comment', 'issues')  # コメントと課題の検索を可能にする
    list_filter = ('issues', 'user')  # 課題とユーザーでのフィルタリングを追加


# UploadFileモデルにエクスポート機能を追加
@admin.register(UploadFile)
class UploadFileAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('id', 'title', 'filename', 'uploaded_at', 'issue')
    search_fields = ('title', 'issue')  # ファイル名と課題の検索を可能にする