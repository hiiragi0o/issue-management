from django.urls import path

from . import views

urlpatterns = [
    path('', views.IssuesListView.as_view(), name='list'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>/', views.IssuesDetailView.as_view(), name='detail'),
    path('create/', views.IssuesCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.IssuesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.IssuesDeleteView.as_view(), name='delete'),
    path('comment/create/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('upload/<int:pk>/', views.FileFieldFormView.as_view(), name='upload'),# 添付ファイル
]