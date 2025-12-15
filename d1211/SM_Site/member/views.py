from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Member


# 로그인 페이지
def login(request):
    if request.method=='GET':
        # 쿠키 읽기
        cook_id= request.COOKIES.get("cook_id","")
        context= {"cook_id":cook_id}
        return render(request,'member/login.html',context)
    elif request.method=='POST':
        id= request.POST.get("id")
        pw= request.POST.get("pw")
        cook_keep= request.POST.get("cook_keep")
        qs= Member.objects.filter(id=id,pw=pw)
        if qs:
            print("아이디와 비밀번호가 일치합니다.")
            # 섹션 저장
            # [키]= 값(input 값)
            request.session['sesssion_id']= id
            context = {"error":"1"}
            # 쿠키 저장해서 페이지로 보낼 저장소 변수를 하나 만듬
            response= render(request,'member/login.html',context)
            
            # 쿠키 저장
            if cook_keep:
                response.set_cookie("cook_id",id,max_age=60*60*24*30)
            else:
                response.delete_cookie("cook_id")
            # 페이지 이동해라
            return response
        else:
            print("아이디와 비밀번호가 일치하지 않습니다.")
            context = {"error":"0"}
            return render(request,'member/login.html',context)

def logout(request):
   # 섹션 삭제
    request.session.clear() # 섹션 모두삭제
    context= {"error":"-1"}
    return render(request,'member/login,html',context)


#-------------------------------------------------------------
# 회원전체리스트 페이지
def list(request):
    qs= Member.objects.all().order_by('-mdate')
    context= {"list":qs}
    return render(request,'member/list.html',context)


# 회원등록 페이지
def write(request):
    if request.method=='GET':
        return render(request,'member/write.html')
    elif request.method=='POST':
        id= request.POST.get("id")
        pw= request.POST.get("pw")
        name= request.POST.get("name")
        phone= request.POST.get("phone")
        gender= request.POST.get("gender")
        hobby= request.POST.getlist("hobby")
        Member.objects.create(id=id,pw=pw,name=name,phone=phone,gender=gender,hobby=hobby)
        print("post 확인: ",id)
        return redirect('/')
