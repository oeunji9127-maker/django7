# sm_pgt: board(개시판).view/view2

# # 게시판 상세보기 - 해당 하단댓글도 함께 가져올수 있음.
# def view(request,bno):
#     # 게시글 가져오기
#     qs = Board.objects.filter(bno=bno)
#     # 하단댓글
#     c_qs = Comment.objects.filter(board=qs[0])
#     # 조회수 1증가
#     # 조회를 한후 조회된 데이터들을 update,delete : F
#     qs.update(bhit = F('bhit') + 1 )
#     context = {'board':qs[0],'clist':c_qs}
#     return render(request,'board/view.html',context)

# # 게시판 상세보기 - 해당 하단댓글도 함께 가져올수 있음.
# def view2(request,bno):
#     print("bno : ",bno)
#     # 게시글 가져오기
#     qs = Board.objects.filter(bno=bno)
#     # 하단댓글
#     c_qs = Comment.objects.filter(board=qs[0]).order_by('-cno')
#     context = {'board':qs[0],'clist':c_qs}
#     return render(request,'board/view2.html',context)


# # 게시판 답글달기
# def reply(request,bno):
#     if request.method == 'GET':
#         # 게시글 가져오기
#         qs = Board.objects.get(bno=bno)
#         context = {'board':qs}
#         return render(request,'board/reply.html',context)
#     elif request.method == 'POST':
#         # 답글저장
#         bgroup = request.POST.get('bgroup')
#         bstep = int(request.POST.get('bstep'))
#         bindent = int(request.POST.get('bindent'))
#         btitle = request.POST.get('btitle')
#         bcontent = request.POST.get('bcontent')
#         id = request.session.get('session_id')
#         member = Member.objects.get(id=id)
#         bfile = request.FILES.get('bfile','')
#         # 1. 답글달기 : 우선 같은 그룹에 있는 게시글의 bstep 1씩 먼저 증가
#         board_qs = Board.objects.filter(bgroup=bgroup,bstep__gt = bstep)
#         board_qs.update(bstep=F('bstep')+1) # F함수 : 검색된 그 컬럼에만 값을 적용
        
#         # 2. 답글저장
#         Board.objects.create(btitle=btitle,bcontent=bcontent,member=member,bgroup=bgroup,\
#             bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        
        
#         context = {'flag':1}
#         return render(request,'board/reply.html',context)


# # 게시판 수정
# def update(request,bno):
#     if request.method == 'GET':
#         # 게시글 가져오기
#         qs = Board.objects.get(bno=bno)
#         context = {'board':qs}
#         return render(request,'board/update.html',context)
#     elif request.method == 'POST':
#         id = request.session.get('session_id')
#         member = Member.objects.get(id=id)
#         btitle = request.POST.get('btitle')
#         bcontent = request.POST.get('bcontent')
#         bfile = request.FILES.get('bfile')
#         # 수정
#         qs = Board.objects.get(bno=bno)
#         qs.btitle = btitle
#         qs.bcontent = bcontent
#         if bfile: qs.bfile = bfile
#         qs.save()    
#         return redirect(f'/board/view/{bno}/')    
                
# # 게시판 삭제
# def delete(request,bno):
#     # 게시글 가져오기
#     qs = Board.objects.get(bno=bno)
#     qs.delete()
#     context = {'flag':2}
#     return redirect("/board/list/")

