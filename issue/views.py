from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Issues, ProgressComment
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from .forms import SignUpForm,LoginForm, CommentCreateForm  # ログインフォームをimport

    
class IssuesListView(LoginRequiredMixin, ListView):
    template_name = 'list.html' # htmlの命名
    model = Issues # どのモデルを引用するか定義

class IssuesDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Issues

    # detail.htmlからコメント投稿
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['comment_form'] = CommentCreateForm

        return context

class IssuesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Issues
    fields = ("title","contents","deadline","type","person","progress","budget")
    # date_of_update は編集不可の項目であるためfieldsに書けない。
    success_url = reverse_lazy("list") # フォーム入力完了後に遷移するURL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IssuesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    model = Issues
    fields = ("title","contents","deadline","type","person","progress","budget")
    # date_of_update は編集不可の項目であるためfieldsに書けない。
    success_url = reverse_lazy("list")

class IssuesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Issues
    success_url = reverse_lazy("list")


class CommentCreate(LoginRequiredMixin, CreateView):
    """
    課題へのコメント作成ビュー
    ページは表示されないが、コメントを作成するために使用
    """
    model = ProgressComment
    form_class = CommentCreateForm

    def form_valid(self, form):
        issues_pk = self.kwargs.get('pk')
        issues = get_object_or_404(Issues, pk=issues_pk)

        progresscomment = form.save(commit=False)# データベース未保存のオブジェクトを返す
        progresscomment.target = issues
        progresscomment.save()

        return redirect('detail', pk=issues_pk)



class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "signup.html" 
    success_url = reverse_lazy("list") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=username, password=password)
        login(self.request, user)
        return response

# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "login.html"

# ログアウトビューを作成
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("list")

