# [ 프로그램 순서 ]


# 1. 프로젝트 생성
# - setting.py 설정
# - 서버 확인

# 2. home 앱 생성
# - setting.py 설정
# - urls.py 설정
# - home>urls.py 설정
# - home>views.py 설정
# - home>template>index.html 파일생성
# - 서버확인

# 3. student 앱 생성
# - setting.py 설정
# - urls.py 설정
# - student >urls.py 설정
# - student >views.py 설정
# - student >template>student>write.html 파일생성
# - 서버확인


# 4. admin 생성
# " DB를 생성하기 전에 makemigrations를 꼭 선언해주어야함"
# " DB를 생성하기 전에, 생성이 가능한지 체크해주는 작업"

# - makemigrations 실행
# - migrate 실행
# - createsuperuser 생성
# - admin 페이지 확인
# http://127.0.0.1:8000/admin

# 5. student>models.py db생성
# - models.py 추가
# - admin.py 추가 : admin페이지에서 보여짐.
# - makemigrations 실행
# - migrate 실행


# model db를 생성하는 페이지
# from django.db import models

# 테이블을 생성하면 항상 id가 자동생성됨: AutoField

#
# class Student(models.Model):
#     sno= models.AutoField(primary_key=True)
#     name= models.CharField(max_length=100)
#     age= models.IntegerField(default=1)
#     grade= models.IntegerField(default=1)
#     gender= models.CharField(max_length=10)
#     hobby= models.CharField(max_length=100,default='게임')
    
#     def __str__(self):
#         return f"{self.sno},{self.name},{self.age},{self.grade},{self.gender}"
#


# 6. student>write.html form생성
# - form html 추가
# - views.py>db 추가(save())
# - admin페이지에서 확인

#
# from django.contrib import admin
# from student.models import Student


# model 페이지 안에 생성한 db를 admin 페이지에 등록해서 보여줌
# admin.site.register(Student)
#



# 7. student>list.html 페이지 생성
# - urls.py 추가
# - views.py 추가
# - db 부분 추가 - Student.objects.all() 추가


# student 앱안에 list함수 부분작성

# 학생리스트함수
# def list(request):
#     qs= Student.objects.all().order_by('-sno')
#     context= {"our_class":"SM유니버스 직무교육","stu_list":qs}
#     return render(request,'student/list.html',context)
#


# - list.html 페이지 확인

# 8. student > view.html 페이지 생성
