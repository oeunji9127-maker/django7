from django.shortcuts import render
from comment.models import Comment
from board.models import Board
from member.models import Member
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse # 전송할때 Json타입으로 변경해서 전송
from django.core import serializers  # Json타입으로 전달된 데이터를 파이썬데이터(set)로 변경

# 하단댓글 수정
def cupdate(request):
    if request.method == 'POST':
        cno = request.POST.get('cno') # 수정버튼을 빵 눌렀을때 가져오는 하단댓글번호
        ccontent = request.POST.get('ccontent') # 수정버튼을 빵 눌렀을때 가져오는 하단댓글내용
        # qs = Comment.objects.get(cno=cno)
        # qs.ccontent = ccontent
        # qs.save()
        
        # json데이터 변환하기 위한 list타입 변경
        Comment.objects.filter(cno=cno).update(ccontent=ccontent) # cno 컬럼명(값없음,의미없음) = 하단댓글번호를 대입함
        # 예를들어, cno가 3번인걸 찾아줘..
        
        c_qs = list(Comment.objects.filter(cno=cno).values())
        # filter(cno=cno) 데이터를 찾기위한 용도일뿐, 정확히 찾고자하는 데이터는 'ccontent'이다
        
        context = {'comment':c_qs[0],'result':'성공'}
        return JsonResponse(context)
    
        # Json 데이터 = Dictionary Type
        # 키와 벨류값으로 데이터형태가 존재
        # context가 '키값과 벨류값'의 형태를 띄고 있으므로 JsonResponse 명령어를 써줌으로써 데이터를 보냄.
    
# 하단댓글 삭제
def cdelete(request):
    if request.method == 'POST':
        cno = request.POST.get('cno')
        Comment.objects.get(cno=cno).delete()
        context = {'result':'성공'}
        return JsonResponse(context)


# 하단댓글 추가 
def cwrite(request):
    if request.method == 'POST':
        id = request.session.get('session_id')
        member = Member.objects.get(id=id)
        bno = request.POST.get('bno')
        board = Board.objects.get(bno=bno)
        cpw = request.POST.get('cpw') 
        ccontent = request.POST.get('ccontent') 
        print(f"bno : {bno}, cpw : {cpw}, ccontent : {ccontent}")
        
        qs = Comment.objects.create(board=board,cpw=cpw,ccontent=ccontent,member=member)
        # print("qs.cno : ",qs)
        # dict_qs = model_to_dict(qs)
        # context = {'comment':dict_qs,'result':'성공'}
        
        # values()를 해야 list타입으로 변경됨.
        c_qs = list(Comment.objects.filter(cno=qs.cno).values())
        context = {'comment':c_qs[0],'result':'성공'}
        return JsonResponse(context)

# 하단댓글 리스트 
def clist(request):
    bno = request.GET.get('bno') 
    print("bno : ",bno)
    board = Board.objects.get(bno=bno)
    qs = Comment.objects.filter(board=board).order_by('-cno')
    list_qs = list(qs.values())  # QuerySet → 리스트
    context = {'result': 'success','list':list_qs}
    return JsonResponse(context)

   