from django.views.generic import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Issues
from django.shortcuts import render
from django.urls import reverse_lazy

    
class IssuesListView(ListView):
    template_name = 'list.html' # htmlの命名
    model = Issues # どのモデルを引用するか定義

class IssuesDetailView(DetailView):
    template_name = 'detail.html'
    model = Issues

class IssuesCreateView(CreateView):
    template_name = 'create.html'
    model = Issues
    fields = ("title","contents","progress_details","deadline","type","person","progress","budget")
    # date_of_update は編集不可の項目であるためfieldsに書けない。
    success_url = reverse_lazy("list") # フォーム入力完了後に遷移するURL

class IssuesUpdateView(UpdateView):
    template_name = 'update.html'
    model = Issues
    fields = ("title","contents","progress_details","deadline","type","person","progress","budget")
    # date_of_update は編集不可の項目であるためfieldsに書けない。
    success_url = reverse_lazy("list")

class IssuesDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Issues
    success_url = reverse_lazy("list")