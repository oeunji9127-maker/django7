# [ 디장고 프로젝트 실행 ]


# 1. 폴더 확인
# cd C:\workspace\django7\d1208
# <cd>

# 2. 프로젝트 생성
# django-admin startproject stupjt01
# <django-admin startproject ~ >

# 3. app생성
# python manage.py startapp student
# <python manage.py startapp ~ >

# 4. stupjt01 > setting.py
# INSTALLED_APPS -> 앱등록을 해야 함.

# 5. urls.py
# from django.urls import path,include
# <include 추가>

# urlpatterns 부분에
# path('student/', include('student.urls')), 추가

# 6. student app > urls 이동
# from . import views 상단추가
# <폴더 안의 모든 파일에서 view를 찾아 선언해라>

# app_name='student' 추가, 별칭&닉네임

# urlpatterns에
# path('write/', views.write,name='write'), 추가
# <student앱에 write경로를 적으면 write함수를 호출한다>

# 7. views.py
# def write(request):
#     return render(request,'write.html') 추가
# <request정보를 받아 'write.html' HTML파일을 연다>

# 8. templates 폴더 생성후 > write.html 추가

# 9. 프로젝트 폴더 이동후 > 서버 실행
# <python manage.py runserver>


# <프로젝트 내의 Setting에 아래 내용 기입>

# # 사용언어

# LANGUAGE_CODE = 'ko-kr'
# # 한국표준 시간사용
# TIME_ZONE = 'Asia/Seoul'


# # 정적파일위치 - css,image,js

# STATIC_URL = 'static/'
# STATICFILES_DIR= [
#     os.path.join(BASE_DIR,'static'),
# ]
