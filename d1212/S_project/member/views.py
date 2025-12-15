from django.shortcuts import render,redirect


def login(request):
    if request.method=='GET':
        cook_id= request.COOKIES.get("cook_id","")
        context= {"cook_id":cook_id}
        
        # 쿠키 검색: 쿠키가 있는지 없는지 확인
        # 쿠키정보를 읽어오는 명령어
        cook_id= request.COOKIES.get("cook_id","") # 쿠키 읽어오는 명령어
        context={"cook_id":cook_id}
        return render(request,'member/login.html',context)
    
    elif request.method=='POST':
        
        #login html파일에 있던 input 정보를 request로 읽어옴
        id= request.POST.get("id")
        pw= request.POST.get("pw")
        login_keep= request.POST.get("login_keep") # getlist()
        print("모든 쿠키 읽기: ",request.COOKIES)
        print("post 입력된 데이터: ",id,pw,login_keep)
        
        # 쿠키 저장
        # 쿠키를 변수에 담아 저장해서 home.index로 보내기 위해 변수를 일단 빼서 만듬
        response= redirect("/")
        if login_keep:
            print("쿠키를 저장하고싶음")
            # 변수 저장소에 쿠키정보를 담아둔다
            response.set_cookie("cook_id",id,max_age=60*60*24*30)
        else:
            print("쿠키를 저장하지않음")
            response.delete_cookie("cook_id")
            
        return response
            
        
            
         
    