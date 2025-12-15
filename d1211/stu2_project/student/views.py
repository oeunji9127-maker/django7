from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Student


# 학생정보 입력페이지
def write(request):
    if request.method=='GET':
        return render(request,'student/write.html')
    elif request.method=='POST':
        name= request.POST.get("name")
        age= request.POST.get("age")
        grade= request.POST.get("grade")
        gender= request.POST.get("gender")
        hobby= request.POST.get("hobby")
        
        qs= Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby)
        return redirect(reverse('student:list'))


# 학생목록 리스트페이지
def list(request):
    return render(request,'student/write.html')



# 학생상세보기 페이지
def view(request):
    return render(request,'student/write.html')

