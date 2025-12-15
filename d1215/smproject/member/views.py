from django.shortcuts import render
from .models import Member

def login(request):
    if request.method=='GET':
        return render(request,'member/login.html')
    elif request.method=='POST':
        id= request.POST.get('id')
        pw= request.POST.get('pw')
        
        # 데이터베이스 안에 들어있는 아이디와 비밀번호, 입력한 아이디와 비밀번호가 일치하는지 확인하는 작업
        qs= Member.objects.filter(id=id,pw=pw)
        if qs:
            # 섹션추가 
            request.session['sesssion_id']=id
            request.session['sesssion_name']=qs[0].name
            context={"flag":"1"}
        else: context={"flag":"0","id":id,"pw":pw}
        return render(request,'member/login.html',context)
    
    
def logout(request):
    request.session.clear()
    context={"flag":"-1"}
    return render(request,'member/login.html',context)
