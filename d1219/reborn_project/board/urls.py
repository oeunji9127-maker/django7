from django.urls import path,include
from . import views


app_name='board'
urlpatterns = [
    # 게시판 목록
    path('list/', views.list,name='list'),
    
    # 게시판 작성하기
    path('write/', views.write,name='write'),
    
    # 게시판글 상세보기
    path('view/', views.view,name='view'),
]
