from django.shortcuts import render

# 학생등록 페이지
def write(request):
    return render(request,'write.html')

# 학생리스트 페이지
def list(request):
    return render(request,'list.html')

# 학생뷰 페이지
def view(request):
    return render(request,'view.html')
