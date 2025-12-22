from django.shortcuts import render

# 게시판 목록보기
def list(request):
    return render(request,'board/list.html')

# 게시판글 작성하기
def write(request):
    return render(request,'board/write.html')

# 게시판글 상세보기
def view(request):
    return render(request,'board/view.html')
