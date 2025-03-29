from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.IssuesListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.IssuesDetailView.as_view(), name='detail'),
    path('create/', views.IssuesCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.IssuesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.IssuesDeleteView.as_view(), name='delete'),
]