from django.shortcuts import render

def index(request):
    # 쿠키 읽어오기 - request
    # 쿠키 저장 - response
    
    # 쿠키 검색
    cook_info= request.COOKIES
    print("쿠키모든정보: ",cook_info)
    cook_id= request.COOKIES.get("cook_id","") # 쿠키정보를 읽어오는데 없을때는 빈공백으로 처리해줘
    cook_pw= request.COOKIES.get("cook_pw","")
    print("cook_id 정보: ",cook_id)
    
    # 쿠키 저장 - response
    response= render(request,'index.html')
    # cook_id= aaa
    # 유지시간을 설정하지 없으면, 브라우저 종료시 사라짐. 시간을 설정하면 시간동안 유지
    
    # 쿠키정보가 없을때만 쿠키저장
    if not cook_id:
        # 쿠키정보를 생성해서 저장해둠
        response.set_cookie("smsite_connect","ok")
        response.set_cookie("ip","127.0.0.1",max_age=60*60*24) # 60초*60분*24시간*365일
    return response
