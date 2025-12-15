from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Student

# 학생등록페이지
def write(request):
    if request.method=='GET':
        return render(request,'student/write.html')
    elif request.method=='POST':
        name= request.POST.get("name")
        age= request.POST.get("age")
        grade= request.POST.get("grade")
        gender= request.POST.get("gender")
        hobby= request.POST.getlist("hobby")
        
        # Student db저장
        qs= Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby)
        qs.save()
        
        # return render(request,'student/list.html')
        # html파일만 열어줄 뿐, 주소값은 변하지 않는다
        return redirect(reverse('student:list'))
        # 페이지로 이동되고 주소도 바뀐다


# 학생수정페이지
def update(request,sno):
    if request.method=='GET':
        qs= Student.objects.get(sno=sno)
        context={"stu":qs}
        return render(request,'student/update.html',context)
    elif request.method=='POST':
        name= request.POST.get("name")
        age= request.POST.get("age")
        grade= request.POST.get("grade")
        gender= request.POST.get("gender")
        hobby= request.POST.getlist("hobby")
        
        # Student db저장
        qs= Student.objects.get(sno=sno)
        qs.name= name
        qs.age= age
        qs.grade= grade
        qs.gender= gender
        qs.hobby= hobby
        qs.save()
        # return render(request,'student/list.html')
        # html파일만 열어줄 뿐, 주소값은 변하지 않는다
        return redirect(reverse('student:list'))
        # 페이지로 이동되고 주소도 바뀐다
        
        
def list(request):
    qs= Student.objects.all().order_by('-sno')
    context={'list':qs}
    return render(request,'student/list.html',context)

# 학생상세보기 페이지
def view(request,sno):
    qs= Student.objects.get(sno=sno)
    context={'stu':qs}
    return render(request,'student/view.html',context)


# 학생삭제페이지
def delete(request,sno):
    qs = Student.objects.get(sno=sno)
    qs.delete() # 삭제
    return redirect(reverse('student:list'))
    
