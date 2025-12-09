# [ 데이터베이스 생성 - admin 관리자 등록 ]

# 1. db생성확인
# python manage.py makemigrations

# 2. db생성
# python manage.py migrate

# 3. admin관리자 등록
# python manage.py createsuperuser

# username :
# email address :
# password :
# password(again) :

# - 패스워드 사용여부 확인[Y/N]


# ---------------------------------------------------------

# [ db관련 명령어 - select,insert,update,delete ]

# - python manage.py shell
# - shell 명령어 창으로 이동

# -from member.models import Member

# 1. 데이터입력 및 저장: insert
# qs = Member(id='bbb',pw='1111',name='유관순',age=21,phone='010-1111-1111',gender='여자',hobby='골프')
# qs.save( )

# qs = Member(id='ddd',pw='1111',name='은지짱',age=26,phone='010-3333-1111',gender='남자',hobby='게임')
# qs.save( )

# qs = Member(id='eee',pw='1111',name='영서짱',age=25,phone='010-6666-7777',gender='여자',hobby='베이킹')
# qs.save( )

# qs = Member(id='fff',pw='1111',name='엄마짱',age=50,phone='010-6666-7788',gender='여자',hobby='드라이빙')
# qs.save( )

# qs = Member(id='ggg',pw='1111',name='아빠짱',age=54,phone='010-6666-9977',gender='남자',hobby='등산')
# qs.save( )


# # 입력과 동시에 저장
# Member.objects.create(id='hhh',pw='1111',name='선영이',age=25,phone='010-6666-9977',gender='여자',hobby='쿠킹')
# # 입력과 동시에 저장/객체에 바로 SAVE 하는 방법
# Member(id='iii',pw='1111',name='손나영',age=26,phone='010-6666-9977',gender='여자',hobby='화학연구').save( )

# 데이터입력 방법1. 
# Member(id='aaa',pw='1111',name='홍길동',age=10,phone='010-6666-1177',gender='남자',hobby='동에번쩍 서에번쩍').save( )
# Member(id='bbb',pw='1111',name='유관순',age=19,phone='010-6622-9977',gender='여자',hobby='사회운동').save( )
# Member(id='ccc',pw='1111',name='이순신',age=29,phone='010-6633-9977',gender='남자',hobby='전쟁게임').save( )
# Member(id='ddd',pw='1111',name='강감찬',age=39,phone='010-5566-9977',gender='남자',hobby='리더십게임').save( )
# Member(id='eee',pw='1111',name='김구',age=49,phone='010-9966-9977',gender='남자',hobby='사회운동').save( )


# 데이터입력 방법2.
# Student.objects.create(id='1',name='오은지',age=25,birth='2000-03-11',rank=1)
# Student.objects.create(id='2',name='오영서',age=25,birth='2000-12-01',rank=6)
# Student.objects.create(id='3',name='백은정',age=30,birth='1995-03-14',rank=2)
# Student.objects.create(id='4',name='오덕환',age=30,birth='1995-11-04',rank=9)
# Student.objects.create(id='5',name='손나영',age=20,birth='2005-08-25',rank=8)



# 2. 데이터검색: select

# 모든데이터 검색
# - Member.objects.all()
# - qs= Member.objects.all() >> qs[0] 출력


# * aaa 검색, 1개일때만 사용가능, (2개 검색되면 에러)
# - Member.objects.get(id='aaa')
# - get: 특정된 '하나'의 데이터만을 검색할때 용이


# * 2개이상 검색(1개도 가능): age=20검색
# - Member.objects.filter(age=20)


# 3. 데이터수정

# 1) 먼저 해당데이터를 검색후
# qs= Member.objects.get(id='aaa')/ 데이터검색

# 2) 원하는 컬럼값을 변경
# qs.name='천고은'
# qs.save( )


# 4. 삭제

# 1) 먼저 해당데이터를 검색후
# qs= Member.objects.get(id='aaa')/ 데이터검색

# 2) 데이터 삭제
# qs.delete( )

# 3) 모든데이터 삭제
# Member.objects.all( ).delete( )


# * 파일존재 확인: exist( )

# * 특정글자가 "포함되어" 있는 데이터를 검색하고 싶을때: __contains
#  Member.objects.fillter(name__contains='김')
#  - SQL: select * from Member where  name like '%김%'


# * 시작,끝부분에 있는 것을 검색: __startwith, __endwith
#  Member.objects.filter(name__startswith='유')
#  - SQL: select * from Member where  name like '김%' 

#  Member.objects.filter(name__endswith='찬')
#  - SQL: select * from Member where  name like '%찬'
 

# * gt,gte, lt,lte
# * 크다, 작다, 크거나같다, 작거나같다 비교검색

# - Member.objects.filter(age__gte=21)
# - 나이가 21살보다 크거나 같은 사람의 데이터를 모두 찾아줘

# - Member.objects.filter(age__lt=21)
# - 나이가 21살보다 작은 사람의 데이터를 모두 찾아줘


# * 특정컬럼만 가져오는 검색방법 - 이름만 검색하고자 할때 예를들어
# Member.objects.values('name')

# * 정렬방법 (순차정렬,역순정렬 모두가능)
# Member.objects.order_by('age') 나이 순차정렬
# Member.objects.order_by('-age') 나이 역순정렬
