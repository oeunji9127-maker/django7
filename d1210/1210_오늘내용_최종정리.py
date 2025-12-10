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

# 6. student>write.html form생성
# - form html 추가
# - views.py>db 추가(save())
# - admin페이지에서 확인

# 7. student>list.html 페이지 생성
# - urls.py 추가
# - views.py 추가
# - db 부분 추가 - Student.objects.all() 추가
# - list.html 페이지 확인

# 8. student > view.html 페이지 생성
