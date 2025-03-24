from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.IssuesListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.IssuesDetailView.as_view(), name='detail'),
]