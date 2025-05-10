import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Issues, ProgressComment, UploadFile
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages #　検索結果のメッセージのため追加
from django.db.models import Q # get_queryset()用に追加
from .forms import FileFieldForm, SearchForm, SignUpForm, LoginForm, CommentForm, IssuesForm
    
class IssuesListView(LoginRequiredMixin, ListView):
    template_name = 'list.html' # htmlの命名
    model = Issues # どのモデルを引用するか定義
    paginate_by = 2 # 1ページあたりの表示件数

    def get_queryset(self):
        """ 検索フォーム """
        queryset = self.model.objects.order_by('-id')  # ソート処理。idが新しい順に並べる
        self.form = form = SearchForm(self.request.GET or None)

        if form.is_valid():
            # 期限（from）
            from_deadline = form.cleaned_data.get('from_deadline')
            if from_deadline:
                queryset = queryset.filter(deadline__gte=from_deadline)

            # 期限（to）
            to_deadline = form.cleaned_data.get('to_deadline')
            if to_deadline:
                queryset = queryset.filter(deadline__lte=to_deadline)

            # キーワードで絞り込み
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                # 空欄で区切り、順番に絞る、and検索
                for word in key_word.split():
                    queryset = queryset.filter(title__icontains=word)
            
            # 進捗状況での絞り込み
            progress = form.cleaned_data.get('progress')
            if progress:
                queryset = queryset.filter(progress=progress)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form  # フォームのデータを渡す
        context['now_date'] = datetime.date.today()  # 期限日の判断のため、今日を取得
        return context

class IssuesDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    template_name = 'detail.html'
    model = Issues
    success_message = "ファイルがアップロードされました！" # 添付ファイル

    # detail.htmlからコメント投稿
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['comment_form'] = CommentForm

        return context

class IssuesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Issues
    form_class =  IssuesForm
    
    # success_url = 更新成功したら該当のdetailページに遷移する
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IssuesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    model = Issues
    form_class =  IssuesForm

    # success_url = 更新成功したら該当のdetailページに遷移する
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

class IssuesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Issues
    success_url = reverse_lazy("list")

class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    課題へのコメント作成ビュー
    ページは表示されないが、コメントを作成するために使用
    """
    model = ProgressComment
    form_class = CommentForm

    #　格納する値をチェック
    def form_valid(self, form):
        form.instance.user = self.request.user
        issues_pk = self.kwargs.get('pk')
        issues = get_object_or_404(Issues, pk=issues_pk)

        progresscomment = form.save(commit=False)# データベース未保存のオブジェクトを返す
        progresscomment.issues = issues
        progresscomment.save()

        return redirect('detail', pk=issues_pk)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    """
    課題へのコメント編集ビュー
    ページは表示されないが、コメントを作成するために使用
    """
    model = ProgressComment
    form_class = CommentForm

    #　格納する値をチェック
    def form_valid(self, form):
        form.instance.user = self.request.user
        issues_id = self.kwargs.get('issue_id')
        issues = get_object_or_404(Issues, pk=issues_id)
        comment_id = self.kwargs.get('pk')
        comment = get_object_or_404(ProgressComment, pk=comment_id)

        progresscomment = form.save(commit=False)# データベース未保存のオブジェクトを返す
        progresscomment.save()

        return redirect('detail', pk=issues_id)

class CommentIndexView(ListView):
    model = ProgressComment
    queryset = ProgressComment.objects.order_by('-id')

class SignupView(SuccessMessageMixin, CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "signup.html" 
    success_url = reverse_lazy("list") # ユーザー作成後のリダイレクト先ページ
    success_message = "アカウントが作成されました！"

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

# 添付ファイル
class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "upload.html"

    # success_url = 更新成功したら該当のdetailページに遷移する
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.issue.pk})

    # アップロードファイルの情報をチェック
    def form_valid(self, form):
        # アップロードファイルをリスト型で取得
        files = form.cleaned_data["files"]
        print("ファイルをアップロードしました！") # あとで消す
        print(files)# あとで消す

        # アップロード対象の Issue を取得
        issue_pk = self.kwargs.get('pk')
        self.issue = get_object_or_404(Issues, pk=issue_pk)

        # アップロードファイルを Issue に関連付けて保存
        for file in files:
            # UploadFile作成時に title に file.name を設定
            UploadFile.objects.create(issue=self.issue, file=file, title=file.name)

        return super().form_valid(form)

# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "login.html"

# ログアウトビューを作成
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("list")

