from django.urls import path,include
from . import views


app_name='member'
urlpatterns = [
    # 게시판 목록
    path('login/', views.login,name='login'),
]
