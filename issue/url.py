from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.IssuesListView.as_view(), name='list'),
    path('detail/', views.IssuesDetailView.as_view(), name='detail'),
]