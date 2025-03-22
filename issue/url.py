from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),#views.pyから「HomeView」クラスを読み込み
]