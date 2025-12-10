from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Student


# 학생등록함수
def write(request):
    if request.method == 'GET':
        return render(request,'student/write.html')
    
    elif request.method == 'POST':
        
        # form 폼에서 넘어온 데이터처리
        name= request.POST.get("name")
        age= request.POST.get("age")
        grade= request.POST.get("grade")
        gender= request.POST.get("gender")
        hobby= request.POST.getlist("hobby")
        # hobbys= ",".join(hobby) # 리스트타입을 문자열타입으로 변환하는 방법
        # 리스트타입을 문자열항목에 저장하면 자동으로 형변환됨
        
        # 입력과 동시에 저장
        Student.objects.create(name=name,age=age,grade=grade,gender=gender,hobby=hobby)
        
        print("이름",request.POST.get("name"))
        print("나이",request.POST.get("age"))
        print("학년",request.POST.get("grade"))
        print("성별",request.POST.get("gender"))
        print("취미",request.POST.getlist("hobby"))
        
        
        return redirect(reverse('student:list'))
        # return redirect('/student/list/')
        

# 학생리스트함수
def list(request):
    qs= Student.objects.all().order_by('-sno')
    context= {"our_class":"SM유니버스 직무교육","stu_list":qs}
    return render(request,'student/list.html',context)

# 학생상세보기 함수 - RESTful: 링크자체에 데이터값만을 실어서 보내는 방법
                # GET: 링크에 변수를 설정해 변수에 데이터값을 넣어 데이터를 실어보내는 방법
def view(request,sno):
    
    # GET.get 방식을 많이써라  # 데이터가 없으면 NONE 
    
    # age= request.GET['age'] # 데이터 없으면 에러
    
    print("넘어온 데이터 sno: ",sno)
    qs= Student.objects.get(sno=sno)
    context={"stu":qs}
    return render(request,'student/view.html',context)

# 학생리스트함수
def delete(request):
    return render(request,'student/list.html')
