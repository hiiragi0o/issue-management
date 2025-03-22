from django.views.generic import View
from django.views.generic import ListView
from .models import Issues
from django.shortcuts import render

    
class IssuesListView(ListView):
    template_name = 'list.html' # htmlの命名
    model = Issues # どのモデルを引用するか定義

class IssuesDetailView(ListView):
    template_name = 'detail.html' # htmlの命名
    model = Issues # どのモデルを引用するか定義